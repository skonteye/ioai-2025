# Parcours francais IOAI 2025

Cette arborescence `fr/` est destinee a devenir la version francaise miroir du depot. L'objectif est qu'un eleve francophone puisse suivre les taches avec le meme niveau de comprehension que dans la version anglaise.

## Etat reel de la traduction

La traduction haute fidelite des notebooks IOAI 2025 du concours individuel est terminee. Chaque tache n'est marquee comme verifiee qu'apres comparaison de son notebook francais avec l'original (meme nombre et meme ordre de cellules, code identique, contenu francophone traduit).

| Tache | Notebook francais | Solution francaise | Etat |
|---|---|---|---|
| Tache 1 | [Radar](Individual-Contest/Radar/Radar.ipynb) | [Solution](Individual-Contest/Radar/Solution/Radar_Solution.ipynb) | Verifie |
| Tache 2 | [Comptage de poulets](Individual-Contest/Chicken_Counting/Chicken_Counting.ipynb) | [Solution](Individual-Contest/Chicken_Counting/Chicken_Counting_Solution.ipynb) | Verifie |
| Tache 3 | [Concepts](Individual-Contest/Concepts/Concepts.ipynb) | [Solution](Individual-Contest/Concepts/Concepts_Solution.ipynb) | Verifie |
| Tache 4 | [Appariement d'icones de toilettes](Individual-Contest/Restroom/Restroom.ipynb) | [Solution](Individual-Contest/Restroom/Solution/Restroom_Solution.ipynb) | Verifie |
| Tache 5 | [Authentification de peintures anciennes](Individual-Contest/Antique/Antique.ipynb) | [Solution](Individual-Contest/Antique/Solution/Antique_Solution.ipynb) | Verifie |
| Tache 6 | [Pixel Efficiency](Individual-Contest/Pixel/Pixel.ipynb) | [Solution](Individual-Contest/Pixel/Pixel_Solution.ipynb) | Verifie |

## Regle de fidelite

Les notebooks francais conservent la meme structure, le meme ordre de cellules, le meme code executable, les memes donnees et les memes sorties attendues que la version originale. Seules les cellules Markdown, les commentaires et les instructions destinees aux lecteurs sont traduits en francais. Les chaines fonctionnelles (prompts de modeles, identifiants de jeux de donnees, noms de modeles, cles JSON, labels, etc.) sont conservees a l'identique pour ne pas alterer le comportement du code. Les ressources binaires (images, datasets) ne sont pas dupliquees : les liens relatifs des notebooks francais pointent vers les dossiers originaux.
