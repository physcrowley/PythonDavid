# PythonDavid

Des exemples de projets Python pour tester l'intégration entre REPL.it et GitHub.

Tout semble fonctionner incluant des projets Pygame Zero, simplement en passant la commande typique

```
python <dossier/nom_de_fichier>.py
```

comme l'argument au paramètre `run` dans le fichier `.replit`. Par exemple, `run = "python projet1/projet1.py"`.

>Le paramètre `run` contrôle ce que le bouton "Run ▶" fait dans REPL.it.

## Pygame Zero
La première fois que le programme qui inclut les lignes

```python
import pgzrun

# code du programme

pgzrun.go()
```

est lancé, REPL.it prépare les fichiers nécessaires pour le projet avant de le lancer. Mais les prochaines fois que le projet est lancé, cette préparation n'est pas nécessaire (la configuration est gardée dans les deux fichiers `poetry.lock` et `pyproject.toml`).