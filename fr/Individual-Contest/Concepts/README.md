# Concepts

## 1. Description du probleme

**Concepts** est un jeu de devinette de mots dans lequel les joueurs communiquent des idees a l'aide d'icones visuelles. Il existe deux roles : le **donneur d'indices** et le **devineur**. Les deux joueurs disposent d'un ensemble commun d'icones visuelles, chacune accompagnee d'une description connue.

Le donneur d'indices choisit d'abord un **secret**, c'est-a-dire un mot ou une expression, puis fournit un **indice** en pointant une **sequence ordonnee** d'icones issues de l'ensemble partage. Il n'est pas permis de parler ni d'ecrire.

L'ordre des icones dans l'indice est significatif :

- La **premiere icone** represente en general l'idee principale du secret.
- Les **icones suivantes** apportent du contexte pour preciser ou enrichir le concept principal.

### Exemple 1

Un indice peut etre interprete comme *un lieu ou se deroule un metier qui combat le feu*, autrement dit une **caserne de pompiers**. Si l'ordre des icones est inverse, il peut plutot suggerer *un metier qui combat le feu dans une maison*, donc un **pompier**.

### Exemple 2

Une meme icone peut prendre des sens differents selon le contexte. Par exemple, l'icone coeur peut apparaitre dans un indice qui suggere *un outil utilise par les medecins pour ecouter le coeur*, c'est-a-dire un **stethoscope**. La meme icone coeur peut aussi apparaitre dans un indice qui implique *un personnage fictif a la fois mort et vivant*, donc un **zombie**.

Lors de l'etape a domicile, les concurrents avaient developpe un programme d'IA qui predisait les reponses a partir d'une sequence d'indices. Cette fois, le defi consiste aussi a produire de bons indices afin qu'un autre systeme d'IA puisse deviner le mot-cle cible.

Dans cette version plus complete du jeu, vous pouvez fournir jusqu'a **4 sequences de marqueurs**. Cela permet d'exprimer des idees complexes plus clairement. Le jeu contient aussi certains mots-cles inhabituels pour Concepts, par exemple `International Olympiad`.

## Nouveau format alimente par l'IA

Le devineur humain est remplace par un **devineur IA**.

1. Le mot cible (*label*) est toujours choisi dans un ensemble predefini (`options`).
2. Les indices doivent etre des **sequences ordonnees de marqueurs** choisis exclusivement parmi **118 marqueurs candidats**.

## Terminologie

- **label** : la reponse cible, ou le "secret", a identifier.
- **options** : l'ensemble predefini de candidats parmi lesquels tous les *labels* valides sont choisis.
- **marker** : une icone representant un concept, accompagnee de sa description textuelle.
- **hints** : une **sequence ordonnee** de *markers* fournie au devineur IA pour l'aider a identifier le *label*.

Votre tache consiste a fournir des **hints** pour chaque *label* afin d'aider le **devineur IA** a l'identifier. Le programme doit produire des listes d'identifiants numeriques, et non des chaines de caracteres.

## 2. Jeu de donnees

Le jeu de donnees fourni contient :

1. Un ensemble d'entrainement avec :
   - `train/` : un jeu de donnees Hugging Face avec 30 exemples ; chaque exemple contient `label` et `options`.
   - `hint_descriptions/` : un jeu de donnees Hugging Face contenant 118 marqueurs et leurs descriptions (`ID`, `Description`, `image`).
2. Deux ensembles de test, accessibles uniquement dans l'environnement d'evaluation :
   - `test_a/` : 150 exemples utilises pour le classement A.
   - `test_b/` : 150 exemples utilises pour le score final.

Les deux ensembles de test utilisent la meme structure que l'ensemble d'entrainement.

## 3. Tache

Vous devez developper un programme qui prend en entree :

1. Une chaine `label`, c'est-a-dire le *label* secret.
2. La liste `options`, contenant 100 choix candidats pour le devineur.

Le `label` appartient toujours a `options`.

Le programme doit retourner, pour chaque `label`, une liste de listes d'entiers representant les indices, c'est-a-dire les sequences de marqueurs :

- au plus **4** sequences ;
- au plus **8** entiers par sequence ;
- chaque entier est l'identifiant d'un marqueur.

Les indices sont ensuite transmis a un devineur IA en boite noire. Vous marquez un point si ce devineur identifie correctement le mot-cle secret a partir de vos indices.

## 4. Soumission

Vous devez soumettre un notebook qui genere `submission.zip`, contenant `clues_a.jsonl` et `clues_b.jsonl`, les indices correspondant respectivement aux ensembles de test A et B. Les conventions de nommage et de structure doivent etre respectees exactement.

Les concurrents peuvent joindre des fichiers de modele. Si vous soumettez des fichiers de modele, vous devez creer un jeu de donnees correspondant sur la plateforme Bohrium. Un seul jeu de donnees peut etre soumis pour cette tache et sa taille totale ne doit pas depasser `2GB`.

## 5. Score

Les indices sont evalues avec deux metriques :

### Hits@10

- vaut `1` si le mot secret apparait parmi les 10 premieres propositions de l'IA ;
- vaut `0` sinon.

### NDCG@10

Cette mesure recompense davantage une bonne reponse lorsqu'elle apparait plus haut dans la liste. Si le mot secret est au rang `i` (en partant de 1), alors :

```text
NDCG@10 = 1 / log2(i + 1)
```

Exemples :

- rang 1 -> `1.00`
- rang 2 -> environ `0.63`
- rang 4 -> environ `0.43`
- rang 10 -> environ `0.29`

### Score final

Le score final est :

```text
0.9 * Hits@10 + 0.1 * NDCG@10
```

Cela signifie qu'il est surtout important que le devineur retrouve le mot secret, avec un bonus si la bonne reponse apparait tres tot.

## 6. Baseline et outils disponibles

- Le score maximal obtenu par le comite scientifique pour cette tache est `0.54`.
- Le score de reference du comite scientifique est `0.20`.
- L'environnement contient notamment `vllm`, `sglang` et `unsloth`.
- L'API du devineur IA sert au developpement local, mais elle n'est pas disponible sur les machines d'inference. Elle ne doit donc pas etre appelee dans les notebooks de soumission.

## 7. Contraintes

- Limite maximale de soumissions : **15** soumissions reussies.
- Temps maximal d'execution sur la machine de test : **10 minutes**.
- Taille maximale du jeu de donnees joint : **2GB**.
- Lors de l'etape sur site, la machine de test n'a pas acces a Internet.
- Un jeton donne droit a `12,500` requetes `POST` vers `/guess`, avec une limite de `1000` appels par minute.

## Note de suivi

Ce fichier est une traduction francaise verifiee de l'enonce pedagogique de `Concepts`. Le notebook miroir complet reste a traduire cellule par cellule afin de conserver tout le code executable, les commentaires et les instructions sans perte de fidelite.
