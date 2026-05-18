# Olympiade internationale d'intelligence artificielle (IOAI 2025, Pekin, Chine)

> Langue : **Francais** | [**English**](../README.md)

Cette arborescence `fr/` est la version francaise miroir du depot. L'objectif est qu'un eleve francophone puisse suivre toutes les taches avec le meme niveau de comprehension que dans la version anglaise.

## A propos de l'IOAI 2025

La [**2eme Olympiade internationale d'intelligence artificielle (IOAI 2025)**](https://ioai-official.org/china-2025/) s'est tenue a **Pekin, Chine**, du **2 au 9 aout 2025**, organisee par la **Beijing National Day School (BNDS)** sous le patronage de l'**UNESCO**.

- **Reglement** : le reglement complet couvrant les concours individuel, par equipe et GAITE est disponible [ici](https://ioai-official.org/china-2025/2025-contest-rules/).
- **Syllabus** : le syllabus officiel des sujets d'IA a maitriser est disponible [ici](https://ioai-official.org/china-2025/syllabus-2025/).
- **Defi par equipe** : les details du defi robotique "Future Factory" sont decrits [ici](https://ioai-official.org/team-challenge/).
- **Resultats** : les tableaux de medailles et les classements officiels sont publies [ici](https://ioai-official.org/china-2025/results-2025/).

## Volets traduits dans `fr/`

| Volet | Etat |
|---|---|
| [Concours individuel](Individual-Contest) | Verifie (6 taches, enonces + solutions) |
| [Concours GAITE](GAITE-Contest) | Verifie (taches 4 et 5, descriptions + notebooks baseline et solution) |
| Concours par equipe (Future Factory) | Hors perimetre : pas de contenu human-facing dans le depot source |
| `Translations/` (traductions par equipes nationales) | Hors perimetre : artefacts de traduction existants vers d'autres langues, non re-traduits |
| `At-Home-Round/` (manche d'entrainement a domicile) | A traduire (voir section dediee ci-dessous) |

## Concours individuel

Tous les enonces et solutions du concours individuel sont entierement traduits.

| Tache | Notebook francais | Solution francaise |
|---|---|---|
| Tache 1 | [Radar](Individual-Contest/Radar/Radar.ipynb) | [Solution](Individual-Contest/Radar/Solution/Radar_Solution.ipynb) |
| Tache 2 | [Comptage de poulets](Individual-Contest/Chicken_Counting/Chicken_Counting.ipynb) | [Solution](Individual-Contest/Chicken_Counting/Chicken_Counting_Solution.ipynb) |
| Tache 3 | [Concepts](Individual-Contest/Concepts/Concepts.ipynb) | [Solution](Individual-Contest/Concepts/Concepts_Solution.ipynb) |
| Tache 4 | [Appariement d'icones de toilettes](Individual-Contest/Restroom/Restroom.ipynb) | [Solution](Individual-Contest/Restroom/Solution/Restroom_Solution.ipynb) |
| Tache 5 | [Authentification de peintures anciennes](Individual-Contest/Antique/Antique.ipynb) | [Solution](Individual-Contest/Antique/Solution/Antique_Solution.ipynb) |
| Tache 6 | [Pixel Efficiency](Individual-Contest/Pixel/Pixel.ipynb) | [Solution](Individual-Contest/Pixel/Pixel_Solution.ipynb) |

Ressources annexes traduites :
- [`Individual-Contest/Concepts/README.md`](Individual-Contest/Concepts/README.md) - guide francais de la tache Concepts.
- [`Individual-Contest/Concepts/llm_proxy_tutorial.ipynb`](Individual-Contest/Concepts/llm_proxy_tutorial.ipynb) - tutoriel du proxy LLM officiel.
- [`Individual-Contest/Pixel/README.md`](Individual-Contest/Pixel/README.md) - guide francais de la tache Pixel.

## Concours GAITE

Le concours GAITE est une variante simplifiee du concours individuel, avec indices. Les sources publiques du depot couvrent les taches 4 et 5.

| Tache | Description | Notebook baseline | Notebook solution de reference |
|---|---|---|---|
| Tache 4 - Segmentation combinatoire de mots | [Description](GAITE-Contest/Word_Segmentation/IOAI2025%20GAITE%20Task%204%20Combinatorial%20Word%20Segmentation%20Task%20Description.md) | [Baseline](GAITE-Contest/Word_Segmentation/IOAI2025%20GAITE%20Task%204%20Combinatorial%20Word%20Segmentation%20Baseline.ipynb) | [Solution de reference](GAITE-Contest/Word_Segmentation/IOAI2025%20GAITE%20Task%204%20Combinatorial%20Word%20Segmentation%20Ref%20Result.ipynb) |
| Tache 5 - Detecteur de parole synthetique | [Description](GAITE-Contest/Synthetic_Speech_Detector/IOAI2025%20GAITE%20Task%205%20Synthetic%20Speech%20Detector%20Task%20Description.md) | [Baseline](GAITE-Contest/Synthetic_Speech_Detector/IOAI2025%20GAITE%20Task%205%20Synthetic%20Speech%20Detector%20Baseline.ipynb) | [Solution de reference](GAITE-Contest/Synthetic_Speech_Detector/IOAI2025%20GAITE%20Task%205%20Synthetic%20Speech%20Detector%20Ref%20Result.ipynb) |

## Manche a domicile (At-Home-Round)

Cette manche d'entrainement comprend trois sujets (Chameleon, Radar, Weather), chacun avec un notebook enonce et un notebook solution. **Ces notebooks ne sont pas encore traduits.** Ils sont disponibles dans la version anglaise sous [`../At-Home-Round/`](../At-Home-Round/).

| Sujet | Enonce anglais | Solution anglaise | Statut francais |
|---|---|---|---|
| Chameleon | [Chameleon.ipynb](../At-Home-Round/Chameleon/Chameleon.ipynb) | [Chameleon_Solution.ipynb](../At-Home-Round/Chameleon/Chameleon_Solution.ipynb) | A traduire |
| Radar (manche a domicile) | [Radar.ipynb](../At-Home-Round/Radar/Radar.ipynb) | [Radar_Solution.ipynb](../At-Home-Round/Radar/Radar_Solution.ipynb) | A traduire |
| Weather | [Weather.ipynb](../At-Home-Round/Weather/Weather.ipynb) | [Weather_Solution.ipynb](../At-Home-Round/Weather/Weather_Solution.ipynb) | A traduire |

## Traductions par equipes nationales

Le dossier [`../Translations/`](../Translations/) contient les traductions officielles des enonces du concours individuel (jour 1 et jour 2) preparees par les chefs d'equipe nationaux dans d'autres langues (espagnol, portugais, allemand, chinois, etc.) au format `.docx` et `.pdf`. Ces documents sont des artefacts de traduction deja produits par les equipes officielles vers leurs langues respectives ; ils ne sont pas re-traduits ici.

## Regle de fidelite

Les notebooks francais conservent la meme structure, le meme ordre de cellules, le meme code executable, les memes donnees et les memes sorties attendues que la version originale. Seules les cellules Markdown, les commentaires et les instructions destinees aux lecteurs sont traduits en francais. Les chaines fonctionnelles (prompts de modeles, identifiants de jeux de donnees, noms de modeles, cles JSON, labels, etc.) sont conservees a l'identique pour ne pas alterer le comportement du code. Les ressources binaires (images, jeux de donnees) ne sont pas dupliquees : les liens relatifs des notebooks francais pointent vers les dossiers originaux.

## Configuration de l'environnement

L'environnement officiel utilise Python 3.12.7 et l'ensemble exact des dependances listees dans [`../requirements.txt`](../requirements.txt). Les concurrents ne pouvaient pas installer d'autres bibliotheques externes : seuls ces paquets etaient utilisables.

```bash
# Avec conda (recommande)
conda create -n ioai-2025 python=3.12.7
conda activate ioai-2025
pip install --upgrade pip
pip install --no-deps -r ../requirements.txt
```

L'option `--no-deps` est essentielle pour garantir les memes versions exactes que dans l'environnement du concours.

## Licence

Ce travail est publie sous la licence **Creative Commons Attribution 4.0 International (CC-BY-4.0)**. Vous pouvez le partager et l'adapter, a condition de citer correctement l'origine et de signaler clairement les modifications.
