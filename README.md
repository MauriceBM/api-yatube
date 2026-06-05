# api_yatube

# API Yatube

API REST pour le réseau social Yatube, permettant de gérer des posts, 
des groupes et des commentaires.

## Technologies utilisées

- Python 3.12
- Django 5.1
- Django REST Framework 3.14
- SQLite (base de données)
- JWT / Token Authentication

## Installation et lancement local

1. Cloner le repository :
   ```bash
   git clone https://github.com/MauriceBM/api-yatube.git
   cd api-yatube


## Créer et activer l'environnement virtuel

python -m venv env
source env/Scripts/activate  # Windows
source env/bin/activate    # Linux/MacOS


## Installer les dépendances

pip install -r requirements.txt


## Appliquer les migrations

cd yatube_api
python manage.py migrate


## Lancer le serveur

python manage.py runserver