from datasets import Dataset
import safetensors
import os
import safetensors.torch
from safetensors import safe_open
import math
import json
if os.environ.get('DATA_PATH'):
    DATA_PATH = os.environ.get("DATA_PATH")  + "/"
else:
    print("No DATA_PATH")
_PRIV_DATASET_KEY = DATA_PATH + "48184d3e-9275-4b29-b571-ade67b9c2fa5"
_A_SET_KEY =  "a_59695b1d-061a-4dc8-bfe5-0b6d2ef7bb68"
_B_SET_KEY =  "b_e898d091-5eb7-48ba-b8ba-0c05ad58caee"

def score(guesses: list[str], gold: str):
    # Normalize to lowercase
    guesses = [g.lower() for g in guesses[:10]]
    gold = gold.lower()

    result = {
        "hits@10": 0.0,
        "ndcg@10": 0.0,
        "total_score": 0.0
    }

    if gold in guesses:
        rank = guesses.index(gold)
        result["hits@10"] = 1.0
        result["ndcg@10"] = 1.0 / math.log2(rank + 2)  # rank + 2 because index is 0-based
    else:
        result["hits@10"] = 0.0
        result["ndcg@10"] = 0.0

    result["total_score"] = 0.9 * result["hits@10"] + 0.1 * result["ndcg@10"]
    return result

def verify_large_model_files():
    """
    Scans current directory for directories or files larger than 50MB,
    uses safetensors to parse them, and ensures parameter count <= 1B.
    
    Returns:
        tuple: (bool, str) - (success, failure_reason)
    """
    # Items to ignore during scanning
    ignore_list = {".venv", "submission.zip"}
    def get_size(path):
        """Get size of file or directory in bytes"""
        if os.path.isfile(path):
            return os.path.getsize(path)
        elif os.path.isdir(path):
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    try:
                        total_size += os.path.getsize(filepath)
                    except (OSError, IOError):
                        pass  # Skip files that can't be accessed
            return total_size
        return 0
    
    def count_parameters_from_safetensors(file_path):
        """Count parameters in a safetensors file"""
        try:
            total_params = 0
            with safe_open(file_path, framework="pt", device="cpu") as f:
                for key in f.keys():
                    tensor = f.get_tensor(key)
                    total_params += tensor.numel()
            return total_params
        except Exception as e:
            raise Exception(f"Failed to parse safetensors file {file_path}: {str(e)}")
    
    # Scan current directory
    current_dir = "."
    large_items = []
    
    # Check all items in current directory
    for item in os.listdir(current_dir):
        # Skip items in ignore list
        if item in ignore_list:
            continue
            
        item_path = os.path.join(current_dir, item)
        item_size = get_size(item_path)
        
        # 50MB = 50 * 1024 * 1024 bytes
        if item_size > 50 * 1024 * 1024:
            large_items.append((item_path, item_size))
    
    if not large_items:
        print("No directories or files larger than 50MB found")
        return True, ""
    
    print(f"Found {len(large_items)} large items (>50MB):")
    for item_path, size in large_items:
        print(f"  {item_path}: {size / (1024*1024):.2f} MB")
    
    # Process each large item
    for item_path, size in large_items:
        try:
            total_params = 0
            safetensors_files = []
            
            if os.path.isfile(item_path):
                # Check if it's a safetensors file
                if item_path.endswith('.safetensors'):
                    safetensors_files.append(item_path)
                else:
                    failure_reason = f"{item_path} is not a safetensors file"
                    print(f"FAILURE: {failure_reason}")
                    return False, failure_reason
            elif os.path.isdir(item_path):
                # Look for safetensors files in the directory
                for root, dirs, files in os.walk(item_path):
                    for file in files:
                        if file.endswith('.safetensors'):
                            safetensors_files.append(os.path.join(root, file))
                
                if not safetensors_files:
                    failure_reason = f"No safetensors files found in directory {item_path}"
                    print(f"FAILURE: {failure_reason}")
                    return False, failure_reason
            
            # Count parameters from all safetensors files
            for safetensors_file in safetensors_files:
                try:
                    params = count_parameters_from_safetensors(safetensors_file)
                    total_params += params
                    print(f"  {safetensors_file}: {params:,} parameters")
                except Exception as e:
                    failure_reason = str(e)
                    print(f"FAILURE: {failure_reason}")
                    return False, failure_reason
            
            # Check if total parameters <= 1B
            if total_params > 1_000_000_000:
                failure_reason = f"Parameter count {total_params:,} exceeds 1B limit for {item_path}"
                print(f"FAILURE: {failure_reason}")
                return False, failure_reason
            
            print(f"✓ {item_path}: Total {total_params:,} parameters (within 1B limit)")
            
        except Exception as e:
            failure_reason = f"Error processing {item_path}: {str(e)}"
            print(f"FAILURE: {failure_reason}")
            return False, failure_reason
    
    print("✓ All large files/directories verified successfully")
    return True, ""

def calc_score():
    verified, failure_reason = verify_large_model_files()
    if not verified:
        error_msg = f"Model files are not verified: {failure_reason}"
        print(error_msg)
        return {
            "public_a": 0,
            "score_a_detail": {
                "error": error_msg
            },
            "private_b": 0,
            "score_b_detail": {
                "error": error_msg
            }
        }
    
    try:
        from submission_model import guess_words
        print("Inference function loaded")
        testset_a = Dataset.load_from_disk(f"{_PRIV_DATASET_KEY}/{_A_SET_KEY}")
        testset_b = Dataset.load_from_disk(f"{_PRIV_DATASET_KEY}/{_B_SET_KEY}")

        def run_eval(dataset: Dataset):
            guesses = []
            total_scores = 0.0
            for example in dataset:
                guesses.append(guess_words(example['hints'], example['options']))
                total_scores += score(guesses[-1], example['label'])['total_score']
            return total_scores / len(dataset)
        
        print("Running Evaluation on Testset A...")
        score_a = run_eval(testset_a)
        if score_a > 1:
            score_a = 0
        print("Running Evaluation on Testset B...")
        score_b = run_eval(testset_b)
        if score_b > 1:
            score_b = 0
        print(f"Score A: {score_a}, Score B: {score_b}")
        return {
            "public_a": score_a,
            "private_b": score_b,
        }
    except Exception as e:
        print(f"Encountered Unexpected Error: {e}")
        return {
            "public_a": 0,
            "private_b": 0,
        }


if __name__ == "__main__":
    score = calc_score()
    ret_json = {
        "status": True,
        "score": score,
        "msg": "Success!",
    }
    with open("score.json", "w") as f:
        json.dump(ret_json, f)