import numpy as np
import torch
import json
import os

TRAIN_PATH = "/bohr/train-ma50/v2/"
if os.environ.get('METRIC_PATH'):
    DATA_PATH = os.environ.get("METRIC_PATH")  + "/"
else:
    print("No METRIC_PATH")

TEST_A = TRAIN_PATH + "dataset.npz"
TEST_B = DATA_PATH + "Y_test.npz"

def main(data_path, pred_path):
    test = np.load(data_path)

    Y_test = {
        128: torch.from_numpy(test['Y_test_128']),
        256: torch.from_numpy(test['Y_test_256']),
    }

    pred = np.load(pred_path)

    Y_pred = {
        128: torch.from_numpy(pred['Y_pred_128']),
        256: torch.from_numpy(pred['Y_pred_256']),
    }

    total_iou = 0.0
    total_dice = 0.0
    total_prec = 0.0
    total_recall = 0.0
    total_data = 0

    rain_y_true = np.array([])
    rain_y_pred = np.array([])

    for patch_size in Y_test.keys():
        for y_pred, y_true in zip(Y_pred[patch_size], Y_test[patch_size]):
            intersection = (y_pred * y_true).sum()
            union = ((y_pred + y_true) > 0).float().sum()
            iou = (intersection / (union + 1e-6)).mean().item()
            dice = (2 * intersection / (y_pred.sum() + y_true.sum() + 1e-6)).mean().item()
            tp = (y_pred * y_true).sum().item()
            fp = (y_pred * (1 - y_true)).sum().item()
            fn = ((1 - y_pred) * y_true).sum().item()
            precision = tp / (tp + fp + 1e-6)
            recall = tp / (tp + fn + 1e-6)

            total_iou += iou
            total_dice += dice
            total_prec += precision
            total_recall += recall
            total_data += 1
            rain_y_true = np.append(rain_y_true, (y_true>0.5).any().cpu().item())
            rain_y_pred = np.append(rain_y_pred, (y_pred>0.5).any().cpu().item())

    if total_data == 0:
        print("⚠️No data")
        return

    acc = (rain_y_true == rain_y_pred).astype(float).mean().item()

    dice_final = total_dice / total_data

    print(f"IoU: {total_iou / total_data:.4f}")
    print(f"Dice: {dice_final:.4f}")
    print(f"Prec: {total_prec / total_data:.4f}")
    print(f"Recall: {total_recall / total_data:.4f}")
    print(f"Image-level Rain Acc: {acc:.4f}")
    total_score = (dice_final + acc) / 2
    print(f"Final score: {total_score:.4f}")

    return total_score

if __name__ == "__main__":
    score_a = main(TEST_A, "pred_a.npz")
    if score_a > 1:
        score_a = 0
    score_b = main(TEST_B, "pred_b.npz")
    if score_b > 1:
        score_b = 0
    if score_a is not None and score_b is not None:
        ret_json = {
            "status": True,
            "score": {
                "public_a": score_a,
                "private_b": score_b,
            },
            "message": "Success",
        }
        with open("score.json", "w") as f:
            json.dump(ret_json, f)
    else:
        ret_json = {
            "status": False,
            "score": {
                "public_a": 0,
                "private_b": 0,
            },
            "message": "⚠️No data points",
        }
        with open("score.json", "w") as f:
            json.dump(ret_json, f)