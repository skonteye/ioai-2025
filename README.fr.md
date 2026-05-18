# Olympiade Internationale d'Intelligence Artificielle (IOAI 2025, Beijing, Chine)

> Langue : **Francais** | [**English**](README.md)

## A propos de l'IOAI 2025

La [**2e Olympiade internationale d'intelligence artificielle (IOAI 2025)**](https://ioai-official.org/china-2025/) s'est tenue a **Beijing, en Chine**, du **2 au 9 aout 2025**, organisee par **Beijing National Day School (BNDS)** sous le patronage de l'**UNESCO**.

- **Reglement du concours** : les regles completes couvrant les concours Individuel, Equipe et GAITE sont disponibles [ici](https://ioai-official.org/china-2025/2025-contest-rules/).  
- **Syllabus** : le syllabus officiel presentant les themes d'IA a maitriser est disponible [ici](https://ioai-official.org/china-2025/syllabus-2025/).  
- **Defi par equipe** : les details du challenge robotique « Future Factory » sont disponibles [ici](https://ioai-official.org/team-challenge/).  
- **Resultats** : les tableaux officiels de medailles et les resultats par pays sont publies [ici](https://ioai-official.org/china-2025/results-2025/).  

## Points forts

- **Concours individuel** : competition sur site en deux jours, precedee d'une phase a domicile (entrainement), axee sur le machine learning, le NLP, la vision par ordinateur, etc.  
- **Defi par equipe** : challenge oriente robotique « Future Factory », avec une phase simulee puis une finale sur robots reels Galbot.  
- **Concours GAITE** : variante simplifiee du concours individuel, avec systeme d'indices, pour une accessibilite plus large.  

## Taches du concours individuel

| Dossier | Enonce de la tache | Solution de reference |
|-------------|-----------|------------------|
| [Tache 1](Individual-Contest/Radar) | [Radar](Individual-Contest/Radar/Radar.ipynb) | [Solution](Individual-Contest/Radar/Solution/Radar_Solution.ipynb) |
| [Tache 2](Individual-Contest/Chicken_Counting) | [Comptage de poulets](Individual-Contest/Chicken_Counting/Chicken_Counting.ipynb) | [Solution](Individual-Contest/Chicken_Counting/Chicken_Counting_Solution.ipynb) |
| [Tache 3](Individual-Contest/Concepts) | [Concepts](Individual-Contest/Concepts/Concepts.ipynb) | [Solution](Individual-Contest/Concepts/Concepts_Solution.ipynb) |
| [Tache 4](Individual-Contest/Restroom) | [Appariement d'icones de sanitaires](Individual-Contest/Restroom/Restroom.ipynb) | [Solution](Individual-Contest/Restroom/Solution/Restroom_Solution.ipynb) |
| [Tache 5](Individual-Contest/Antique) | [Authentification de peinture ancienne](Individual-Contest/Antique/Antique.ipynb) | [Solution](Individual-Contest/Antique/Solution/Antique_Solution.ipynb) |
| [Tache 6](Individual-Contest/Pixel) | [Efficacite Pixel](Individual-Contest/Pixel/Pixel.ipynb) | [Solution](Individual-Contest/Pixel/Pixel_Solution.ipynb) |

## Configuration de l'environnement

L'environnement de competition utilise Python 3.12.7 et inclut un ensemble complet de dependances listees dans [requirements.txt](requirements.txt). Les participants n'etaient pas autorises a installer d'autres bibliotheques externes. Voici les instructions de configuration avec differents gestionnaires de paquets.

### Avec Conda (recommande)

```bash
# Create and activate a new conda environment
conda create -n ioai-2025 python=3.12.7
conda activate ioai-2025

# Update pip and install dependencies
pip install --upgrade pip
pip install --no-deps -r requirements.txt
```

### Avec venv

```bash
# Linux/macOS
python3.12 -m venv ioai-2025
source ioai-2025/bin/activate

# Windows
python -m venv ioai-2025
.\ioai-2025\Scripts\activate

# Install dependencies (all platforms)
pip install --upgrade pip
pip install --no-deps -r requirements.txt
```

### Avec pyenv

```bash
# Install Python 3.12.7
pyenv install 3.12.7
pyenv local 3.12.7

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.\.venv\Scripts\activate   # Windows

# Install dependencies
pip install --upgrade pip
pip install --no-deps -r requirements.txt
```

> **Note** : l'option `--no-deps` est necessaire pour garantir des versions de paquets identiques a l'environnement officiel du concours.

## Traductions des taches du concours individuel

Des versions traduites des enonces du concours individuel sont disponibles pour le [Jour 1](Translations/Individual-Contest-Day1) et le [Jour 2](Translations/Individual-Contest-Day2).  

Ces traductions ont ete preparees de maniere optionnelle par les Team Leaders et fournies a leurs participants pendant le concours, en complement de la version officielle en anglais.

## Auteurs des taches et contributeurs

### Concours individuel
- **Tache 1 – Radar** : equipe de **Peking University**  
- **Tache 2 – Prevision meteo satellite & comptage de poulets** : **Evgenii Tsymbalov (At-Home)** et equipe de **Shenzhen University (On-Site)**  
- **Tache 3 – Concepts** : **Alham Aji**  
- **Tache 4 – Appariement d'icones de sanitaires** : equipe de **Beihang University**  
- **Tache 5 – Authentification de peinture ancienne** : **Dong Yixi**, DP Technology  
- **Tache 6 – Defi d'efficacite Pixel** : **Kirill Fedyanin**  

### Concours GAITE
- **Tache 3 – Resonance Elf** : **Ma Chichuan**, Beijing Navigation School  
- **Tache 4 – Segmentation combinatoire de mots** : **Li Yulin**, Microsoft  
- **Tache 5 – Detecteur de voix synthetique** : **Li Yulin**, Microsoft  

### Defi par equipe
- **Factory of the Future** : equipe de **Galbot** et de **Beijing National Day School**  

## Licence

Ce travail est publie sous la licence **Creative Commons Attribution 4.0 International (CC-BY-4.0)**.  
Vous pouvez le partager et l'adapter a condition de crediter correctement la source et d'indiquer clairement les modifications apportees.
