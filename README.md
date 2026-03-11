Projet : Application de gestion d’une bibliothèque de livres (Django)
===============================================================================

Ce dépôt contient une application web Django pour gérer une bibliothèque de livres
(CRUD complet : ajout, affichage, mise à jour et suppression de livres).


1. Prérequis
-------------------------------------------------------------------------------

- Python 3.12 (ou version 3.10+)
- Git (pour cloner le projet)
- Windows (commandes ci‑dessous en PowerShell)


2. Récupération du projet
-------------------------------------------------------------------------------

```bash
git clone <URL_DU_REPO>
cd bibleotheque_livre
cd project
```


3. Création et activation de l’environnement virtuel
-------------------------------------------------------------------------------

Depuis le dossier `project` :

```powershell
python -m venv .venv
.venv\Scripts\activate
```

L’environnement virtuel `.venv` est ignoré par Git (voir `.gitignore`).


4. Installation des dépendances
-------------------------------------------------------------------------------

Pour l’instant, l’application utilise principalement Django :

```powershell
pip install "django==6.0.3"
```

Optionnellement, si un fichier `requirements.txt` est ajouté plus tard :

```powershell
pip install -r requirements.txt
```


5. Initialisation de la base de données
-------------------------------------------------------------------------------

Toujours depuis le dossier `project` (et avec le venv activé) :

```powershell
python manage.py migrate
```

Si tu veux créer un super‑utilisateur Django pour accéder à l’admin :

```powershell
python manage.py createsuperuser
```


6. Lancer le serveur de développement
-------------------------------------------------------------------------------

Toujours avec le venv activé :

```powershell
python manage.py runserver
```

Puis ouvrir le navigateur sur :

- Application : http://127.0.0.1:8000/
- Interface d’administration : http://127.0.0.1:8000/admin/

Pour arrêter le serveur : `CTRL + C` dans le terminal.


7. Structure rapide du projet
-------------------------------------------------------------------------------

- `project/` : dossier Django principal
	- `manage.py` : script de gestion Django
	- `project/` : configuration (settings, urls…)
	- `project_app/` : application principale (modèles, vues…)
	- `templates/` : templates HTML
	- `static/` : fichiers statiques (CSS, JS, images…)


8. Commandes utiles (rappel)
-------------------------------------------------------------------------------

- Activer le venv (depuis `project/`) :
	```powershell
	.venv\Scripts\activate
	```
- Désactiver le venv :
	```powershell
	deactivate
	```

En suivant ces étapes, toute personne peut cloner le dépôt, installer
les dépendances et lancer l’application localement.