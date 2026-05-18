# IOAI2025 GAITE : Segmentation combinatoire de mots
## Note : commencez par "rejoindre" la competition. Vous pourrez ensuite monter le jeu de donnees sur le GPU. Sinon, le notebook risque de produire une erreur car il ne peut pas acceder au jeu de donnees tant que vous n'avez pas rejoint la competition.

## 1. Description du probleme

Les composes, qui designent la formation de nouveaux mots a partir de plusieurs mots courts, sont particulierement frequents en allemand. Par exemple, 'Fussball' est une combinaison de 'Fuss' et 'Ball' (en francais : "pied" et "ballon"). 'Autobahnanschlussstelle' est une combinaison de 'Autobahn', 'Anschluss' et 'Stelle' (autoroute, raccordement, emplacement).

Dans cette question, il faut decouper la combinaison de mots presente dans une phrase allemande en mots courts separes par des espaces. Par exemple, 'Fussballspieler' doit etre decoupe en 'Fuss', 'ball' et 'spieler'.

## 2. Jeu de donnees

L'ensemble d'entrainement (`data/train.json`) contient plus de 90 000 mots composes allemands, chacun ayant deja ete decoupe en mots courts. Chaque entree contient deux champs : le mot compose et l'etiquette de segmentation.

L'ensemble de validation (`val.json`) et l'ensemble de test (`test.json`) contiennent chacun plus de 10 000 mots composes allemands. Les tailles precises sont :

- **Ensemble d'entrainement** : 94 306 entrees, dans `train.json` ;
- **Ensemble de validation** : 11 788 entrees, dans `val.json` ;
- **Ensemble de test** : 11 789 entrees, dans `test.json` ;

Exemple de donnees :

```json
{
    "Sprachbereich": [
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        1
    ],
    "Autobahnanschlussstelle": [
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1
    ],
    ...
}
```

Les donnees sont au format JSON, avec la cle correspondant au mot compose et la valeur etant un tableau de 0 et 1, ou chaque position du tableau correspond a la lettre correspondante du mot compose. Un `1` indique la fin d'un mot court et un `0` indique le debut ou le milieu d'un mot.

Par exemple, la premiere entree indique que 'Sprachbereich' est decoupe en 'Sprach' et 'bereich' : la valeur vaut donc `1` a la position 5 (numerotation a partir de 0) ainsi qu'a la derniere position, et `0` ailleurs.

Les tableaux de 0 et 1 sont vides pour les ensembles de validation et de test.

## 3. Tache

Implementez un decoupeur combinatoire de mots qui remplit le champ de valeur de l'ensemble de validation et de l'ensemble de test.

**Indice : des modeles d'apprentissage profond comme un Embedding suivi d'un LSTM sont recommandes.**

## 4. Soumission

Les concurrents doivent soumettre **le code d'entrainement et d'inference du modele** nomme `submission.ipynb`, qui **doit inclure le processus d'entrainement et le processus de test sur les ensembles de validation et de test**, et pas seulement le modele entraine.

La sortie de `submission.ipynb` est une archive zip contenant deux fichiers, `submissionval.json` et `submissiontest.json`, dans le meme format que l'ensemble d'entrainement, avec les predictions pour `val.json` et `test.json`.

Le [baseline.ipynb](https://ioai.bohrium.com/notebooks/19761983382) fournit le format de soumission.

## 5. Score

Le score final est la **F1-score** moyenne pour chaque mot compose. Le score pour `val.json` peut etre consulte sur le classement A pendant la competition ; le score pour `test.json` n'est pas consultable durant la competition et n'apparait qu'a la fin, et c'est lui qui sera utilise pour le score final avant unification.

**Indice : pas besoin de connaitre la F1-score en detail, comprenez simplement que plus la position predite est exacte, plus le score est eleve.**

## 6. Baseline et ensemble d'entrainement

- Le baseline se trouve dans [baseline.ipynb](https://ioai.bohrium.com/notebooks/19761983382).
- Le jeu de donnees est disponible dans le [training set](https://ioai.bohrium.com/competitions/5115012331?tab=datasets).

## 7. Contraintes

- Limite maximale de soumissions : **50 fois**. Seules les soumissions reussies (celles qui recoivent un score sur le classement A) comptent dans cette limite.

- Restrictions de l'environnement de test : la machine de test execute votre notebook en **20 minutes** maximum. Si l'execution depasse **20 minutes**, le systeme l'interrompt et renvoie une indication "Timeout" ou "Failed".

- Soumission de donnees et de modeles : pour cette tache, les concurrents peuvent uniquement soumettre un notebook et ne peuvent joindre ni jeu de donnees monte ni fichier `.pth` produit par eux-memes. Pensez a retirer le jeu de donnees monte dans le coin superieur droit.

  ![alt](https://minio-ioai.bohrium.com/bohrium/article/74628/fdbf5cb4c1ec4c5e97f821a21929614b/35d423b5-6af7-4b26-8c42-f395aca052e5.png)

- Reseau : lors de l'etape sur site, la machine de test n'a pas acces a Internet. Les commandes de telechargement comme `pip` ou `conda`, ainsi que les appels d'API, ne fonctionnent pas.

- Modeles pre-entraines : tout modele pre-entraine peut etre utilise des lors qu'il peut etre importe correctement sans connexion reseau ni telechargement. Cela signifie que Bohrium ne peut pas garantir l'exclusion totale des modeles pre-entraines dans l'image Python lors de l'installation des paquets ; lorsque vous en trouvez d'utiles, vous pouvez les utiliser.

## 8. Precautions

- Quel score est pris en compte : les concurrents peuvent selectionner jusqu'a 2 soumissions pour le scoring (V - selectionne, vide - non selectionne). Le score avant unification pour cette tache est determine par le meilleur score sur le classement B parmi les deux soumissions selectionnees. Pour les autres cas, reportez-vous a **Annexe : mecanismes et restrictions de la plateforme pour le concours individuel et le GAITE**.

  ![alt](https://minio-ioai.bohrium.com/bohrium/article/74628/7f7c800250dd4979aff0d7dce8fd6703/3a6274e4-dec9-445a-b899-4f429bec4256.jpeg)

- Si un concurrent ne soumet qu'une seule fois juste avant la fin de la competition, la plateforme attend que le resultat soit calcule et l'utilise pour le score.

- Comment traiter les ambiguites : en cas de conflit entre la description de la tache et le jeu d'entrainement, les donnees du jeu d'entrainement font foi ; le jeu de donnees ne sera pas modifie pendant la competition.

- Les concurrents n'ont acces au classement A que pendant la competition et n'ont pas acces au classement B. Le score final est calcule uniquement a partir du classement B.

- Le meilleur score du comite scientifique pour cette tache est 0.95 sur le classement B ; ce score sert a l'unification.

- Le score baseline du comite scientifique pour cette tache est 0 sur le classement B ; ce score sert a l'unification.

## 9. Indices

Vous pouvez utiliser un LSTM pour resoudre ce probleme. Differentes versions de LSTM donnent des resultats differents.

Le principe est de remplacer le contenu de `class MyModel(nn.Module):` par un LSTM.

Le code du LSTM peut etre obtenu en interrogeant le chatbot de Bohrium.
