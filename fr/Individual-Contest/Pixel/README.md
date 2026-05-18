# Tache Pixel Efficiency IOAI 2025

Ce dossier contient les ressources de la tache Pixel Efficiency (jour 2, tache 6) du concours IOAI 2025.

# Description des fichiers

- `Pixel.ipynb` : le notebook baseline.
- `Pixel_Solution.ipynb` : l'implementation officielle de la solution de reference du HSC et de l'ISC.
- `metrics.py` : le script d'evaluation (utilise le script original, voir [`../../../Individual-Contest/Pixel/metrics.py`](../../../Individual-Contest/Pixel/metrics.py)).

# Utilisation

Executez d'abord `Pixel.ipynb`, `Pixel_Solution.ipynb`, ou toute autre solution que vous souhaitez tester. Ce notebook genere un fichier `submission.jsonl` contenant les masques produits.

Ensuite, lancez `metrics.py` pour evaluer la solution et obtenir les precisions finales.
