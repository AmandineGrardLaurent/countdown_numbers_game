countdown_numbers_game
# 🧮 Countdown numbers game — Jeu Python

Ce programme est une version simplifiée du célèbre jeu **"Le Compte est Bon"**, dans lequel le joueur doit combiner des nombres à l’aide d’opérations mathématiques pour atteindre un nombre cible donné.

---

## 🎯 Objectif du jeu

Le but est d’obtenir **un nombre cible**, compris entre **101** et **999**, en combinant **6 nombres tirés au hasard** avec les opérations `+`, `-`, `*`, et `/`.  
Chaque nombre ne peut être utilisé **qu'une seule fois**. À chaque tour, le joueur choisit deux nombres et une opération pour en créer un nouveau, jusqu'à atteindre le résultat ou ne plus pouvoir jouer.

---

## 🗂️ Fichiers

- `countdown_numbers_game.py` : Le fichier principal contenant toute la logique du jeu.

---

## ▶️ Lancer le jeu

### Prérequis

- Python 3.x installé.

### Exécution

Dans un terminal ou la console de PyCharm :

```bash
python countdown_numbers_game.py
```

---

## 🧠 Règles du jeu

1. **6 cartes (nombres)** sont tirées au hasard depuis une liste prédéfinie :
   - Nombres entre 1 et 10 (deux fois chacun)
   - 25, 50, 75, 100 (une fois chacun)

2. Un **nombre cible** entre 101 et 999 est généré aléatoirement.

3. À chaque tour :
   - Le joueur choisit un **premier nombre**.
   - Il choisit ensuite une **opération** parmi `+`, `-`, `*`, `/`.
   - Il choisit un **deuxième nombre**.
   - Le résultat est calculé et **remplace** les deux nombres choisis dans la liste.

4. Le jeu continue jusqu’à :
   - Ce que le joueur atteigne exactement le nombre cible → **Victoire 🎉**
   - Il ne reste plus qu’un seul nombre sans avoir atteint le résultat → **Défaite ❌**

---

## 🧾 Fonctions principales

#### `draw_starting_cards()` : Tire 6 nombres aléatoires parmi la liste autorisée.

#### `generate_target_number()` : Génère un nombre cible entre 101 et 999.

#### `ask_number(available_numbers)` : Demande à l’utilisateur de choisir un nombre parmi ceux disponibles.

#### `ask_operator()` : Demande à l’utilisateur de choisir une opération valide.

#### `calculator(nb_1, nb_2, operator_symbol)` : Applique l’opération entre deux nombres.

#### `one_turn(available_numbers)` : Exécute un tour : sélection de 2 nombres, choix d’une opération, calcul et mise à jour de la liste.

#### `countdown_numbers_game(available_numbers)` : Boucle principale du jeu jusqu’à la fin.

---

## 📝 Exemple d'exécution

```
Chiffre à atteindre : 742
Choisissez un chiffre parmi les suivants : 1, 3, 10, 25, 50, 75
75

Quelle opération souhaitez-vous réaliser ? [ + , - , * , / ]
+

Choisissez un chiffre parmi les suivants : 1, 3, 10, 25, 50
50

Nouvelle entrée : 125
Chiffre à atteindre : 742
...
```
