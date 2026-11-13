# 🚀 Space Invader

Un clone de Space Invader développé en Python avec Pygame dans le cadre de mon apprentissage de la programmation orientée objet et du développement de jeux vidéo.

---

# ⚙️ Installation

## Cloner le dépôt

```bash
git clone https://github.com/Brukzer/space-invader.git
```

## Se placer dans le projet

```bash
cd space-invader
```

## Installer les dépendances

```bash
pip install pygame
```

---

# ▶️ Lancement

```bash
python main.py  
```

---

# 📖 Sommaire

- Présentation
- Fonctionnalités
- Captures d'écran
- Technologies utilisées
- Lancement
- Contrôles
- Structure du projet
- Architecture
- Roadmap
- Améliorations futures
- Auteur
- Licence

---

# 🎮 Présentation


# ✨ Fonctionnalités

## Fonctionnalités actuelles

- Déplacement du joueur
- Tir de projectiles
- Apparition des ennemis
- Détection des collisions
- Suppression des ennemis éliminés
- Affichage du jeu en temps réel

## Fonctionnalités prévues

- Système de score
- Barre de vie
- Plusieurs types d'ennemis
- Boss de fin de niveau
- Power-ups
- Menu principal
- Sauvegarde des scores

---

# 🛠️ Technologies utilisées

## Langage

- Python 3

## Bibliothèques

- Pygame

## Outils

- Git
- GitHub
- VS Code

# IA

- IA 
---


# 🎯 Contrôles

| Touche | Action |
|----------|----------|
| ← | Déplacement gauche |
| → | Déplacement droite |
| Espace | Tir |
| Échap | Quitter |

---

# 📂 Structure du projet

```text
space-invader/
│
├── main.py
├── affichage.py
├── perso.py
├── ennemi.py
├── arme.py
├── physique.py
│
├── assets/
│   ├── images/
│   ├── sounds/
│   └── fonts/
│
├── README.md
└── .gitignore
```

---

# 🏗️ Architecture

## main.py

Point d'entrée du programme.

Responsabilités :

- Initialisation du jeu
- Boucle principale
- Gestion des événements

## perso.py

Contient la classe du joueur.

Responsabilités :

- Déplacements
- Gestion des tirs
- Statistiques du joueur

## ennemi.py

Contient la logique des ennemis.

Responsabilités :

- Apparition
- Déplacement
- Destruction

## arme.py

Gestion des projectiles.

Responsabilités :

- Création des tirs
- Déplacement des tirs
- Suppression hors écran

## physique.py

Gestion des collisions.

Responsabilités :

- Collision projectile / ennemi
- Collision joueur / ennemi

## affichage.py

Gestion de l'affichage.

Responsabilités :

- Dessin des sprites
- Mise à jour de la fenêtre
- Affichage HUD

---


---

# 🔮 Améliorations futures

=> road map

---

# 👤 Auteur

**Parmentier Luka**
**Roméo ???**

- GitHub : https://github.com/Brukzer

---

# 📜 Licence

Ce projet est distribué sous licence MIT.

Vous êtes libre de :

- Utiliser
- Modifier
- Distribuer

Le projet est fourni sans garantie, mais avec des excuse pour le pseudo pourri du github.

---
⭐ Si le projet vous plaît, n'hésitez pas à laisser une étoile sur GitHub !


Petit conseil : ajoute aussi un fichier .gitignore pour éviter d'envoyer .idea, __pycache__, .venv, etc. sur GitHub. C'est l'une des premières choses que les recruteurs regardent sur un dépôt Python.