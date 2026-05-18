# IOAI2025 GAITE : Detecteur de parole synthetique

## Note : commencez par "rejoindre" la competition. Vous pourrez ensuite monter le jeu de donnees sur le GPU. Sinon, le notebook risque de produire une erreur car il ne peut pas acceder au jeu de donnees tant que vous n'avez pas rejoint la competition.

## 1. Description du probleme

Dans la vie reelle, la parole synthetique (parole generee par IA) est aujourd'hui largement utilisee. Si cette technologie a connu des avancees significatives, elle souleve aussi des inquietudes quant a son detournement, comme la fabrication de fausses pistes audio de personnalites publiques ou la diffusion de messages vocaux trompeurs. La capacite a distinguer la parole synthetique de la parole humaine reelle est essentielle pour de nombreuses applications : verification de contenu, securite, et considerations ethiques pour les medias generes par IA. Le developpement rapide des modeles generatifs rend la distinction entre enregistrements synthetiques et humains de plus en plus difficile. Ce projet vise a developper un modele capable de distinguer efficacement ces deux types d'echantillons audio.

## 2. Jeu de donnees

Les donnees brutes utilisees dans ce projet consistent en des fichiers audio de parole humaine et de parole synthetique. Cependant, les fichiers audio ne pouvant pas etre utilises directement pour l'entrainement, l'audio est d'abord converti en spectrogramme de Mel. Visuellement, cela ressemble a une image 2D avec le temps en abscisse et la frequence de Mel en ordonnee.

![alt](https://minio-ioai.bohrium.com/bohrium/article/73760/ec7a27b861c745d9be29d86fe87a968f/7c69b573-30ea-4d51-9838-320ed505d5b4.png)

Cette conversion etant fastidieuse, le jeu de donnees fourni est constitue de spectrogrammes de Mel pre-convertis a partir des fichiers audio bruts, plutot que des audios eux-memes. Ces spectrogrammes sont tous sauvegardes sous forme de tenseurs au format `.pt`. Les donnees d'entrainement sont disponibles [ici](https://ioai.bohrium.com/competitions/5115013137?tab=datasets). Les fichiers dont le nom contient `bonafide` correspondent aux spectrogrammes d'enregistrements humains reels, tandis que le dossier `spoof` contient tous les spectrogrammes de parole synthetique.

Notez que la classe `SpectrogramDataset` dans [baseline.ipynb](https://ioai.bohrium.com/notebooks/93479335231) est celle utilisee pour lire les donnees d'entrainement. **Ne la modifiez pas pour eviter des erreurs de chargement**. Cette classe est principalement concue pour charger les spectrogrammes et fournit les scripts necessaires pour implementer l'interface `Dataset` de PyTorch lors de l'entrainement des modeles. Elle parcourt les sous-dossiers de chaque jeu de donnees et aide a l'etiquetage (`bonafide` etiquete `0`, `spoof` etiquete `1`). Sa methode magique `__getitem__` renvoie un dictionnaire de la forme `{ 'spectrogram': Tensor, 'label': Tensor, 'path': str }`, ou `spectrogram` est le tenseur de spectrogramme, `label` le tenseur d'etiquette, et `path` le chemin du fichier.

## 3. Tache

(1) Votre objectif est de developper un modele capable de distinguer la parole synthetique (generee par IA) des enregistrements humains reels. Vous pouvez utiliser un modele ResNet18.

**(2) Conseils :** si vous choisissez des modeles visuels plus grands que ResNet18, il faut maitriser le nombre d'epoques d'entrainement : le baseline n'entraine qu'une seule epoque, ce qui est insuffisant ; mais trop d'epoques peuvent empecher de terminer l'entrainement dans le temps imparti. Vous pouvez aussi traiter cette tache comme un probleme purement de vision par ordinateur et la resoudre avec un CNN implemente par vos soins. Ne vous focalisez pas trop sur les details d'implementation de la conversion en spectrogrammes de Mel, qui peut etre peu pertinente pour la tache.

## 4. Soumission

Les concurrents doivent soumettre un fichier notebook nomme `submission.ipynb`, qui peut ne contenir que le modele entraine en omettant le processus d'entrainement pour permettre un scoring rapide. Il doit produire une archive zip contenant les resultats de prediction, soit deux fichiers :

- `submissionA.csv` : contient les etiquettes predites pour l'ensemble de validation, une valeur 0 ou 1 par ligne, sans entete.
- `submissionB.csv` : contient les etiquettes predites pour l'ensemble de test, une valeur 0 ou 1 par ligne, sans entete.

## 5. Score

Le score est calcule en comparant le CSV soumis par les concurrents avec le fichier `ground_truth_labels.csv`.

La metrique d'evaluation est la **F1-score**.

**Indice : pas besoin de connaitre la F1-score en detail ; intuitivement, plus la position predite est exacte, plus le score est eleve.**

## 6. Baseline et ensemble d'entrainement

- Le baseline se trouve dans [baseline.ipynb](https://ioai.bohrium.com/notebooks/93479335231).
- Le jeu de donnees est disponible dans le [training set](https://ioai.bohrium.com/competitions/5115013137?tab=datasets).

## 7. Contraintes

- Limite maximale de soumissions : **50 fois**. Seules les soumissions reussies (celles qui recoivent un score sur le classement A) comptent dans cette limite.

- Restrictions de l'environnement de test : la machine de test execute votre notebook en **20 minutes** maximum. Si l'execution depasse **20 minutes**, le systeme l'interrompt et renvoie une indication "Timeout" ou "Failed".

- Soumission de donnees et de modeles : pour cette tache, les concurrents peuvent soumettre un notebook ainsi que des jeux de donnees montes ou des fichiers `.pth` produits par eux-memes.

- Reseau : lors de l'etape sur site, la machine de test n'a pas acces a Internet. Les commandes de telechargement comme `pip` ou `conda`, ainsi que les appels d'API, ne fonctionnent pas.

- Modeles pre-entraines : tout modele pre-entraine peut etre utilise des lors qu'il peut etre importe correctement sans connexion reseau ni telechargement.

## 8. Precautions

- Quel score est pris en compte : les concurrents peuvent selectionner jusqu'a 2 soumissions pour le scoring (V - selectionne, vide - non selectionne). Le score avant unification pour cette tache est determine par le meilleur score sur le classement B parmi les deux soumissions selectionnees. Pour les autres cas, reportez-vous a **Annexe : mecanismes et restrictions de la plateforme pour le concours individuel et le GAITE**.
  ![alt](https://minio-ioai.bohrium.com/bohrium/article/74628/7f7c800250dd4979aff0d7dce8fd6703/3a6274e4-dec9-445a-b899-4f429bec4256.jpeg)

- Comment traiter les ambiguites : en cas de conflit entre la description de la tache et les ensembles d'entrainement, de validation ou de test, le jeu de donnees fait foi ; il ne sera pas modifie pendant la competition.
- Les concurrents n'ont acces au classement A que pendant la competition et n'ont pas acces au classement B. Le score final est calcule uniquement a partir du classement B.
- Le meilleur score du comite scientifique pour cette tache est 0.90 sur le classement B ; ce score sert a l'unification.
- Le score baseline du comite scientifique pour cette tache est 0.70 sur le classement B ; ce score sert a l'unification.

## 9. Indices

Vous pouvez suivre les etapes ci-dessous pour completer cette tache :

Executez [baseline.ipynb](https://ioai.bohrium.com/notebooks/93479335231) :
- Dans la definition du modele `class MyModel(nn.Module)`, mettez `model = resnet18(pretrained=ResNet18_Weights)`. Les parametres pre-entraines seront importes automatiquement lors de l'instanciation du modele ; si necessaire, vous pouvez aussi ajuster la structure du modele. Vous pouvez remplacer `model = resnet18(pretrained=ResNet18_Weights)` par un meilleur modele pour obtenir un score plus eleve, par exemple `model = resnet34(pretrained=ResNet34_Weights)`.
- Vous pouvez egalement augmenter le nombre d'epoques pour obtenir un meilleur score. Entrainez le modele sur plusieurs epoques avec l'ensemble d'entrainement. Normalement, la perte de validation diminue continuellement ; si necessaire, ajustez les parametres d'entrainement (nombre d'epoques, taille de batch, taux d'apprentissage).
