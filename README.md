# 📚 Système de Gestion de Bibliothèque

Application web complète pour la gestion d'une bibliothèque, développée avec Flask et PostgreSQL.

![Page d'accueil](img/2png)

## 🎯 Fonctionnalités

### Gestion des Livres
- Ajouter, modifier et supprimer des livres
- Rechercher des livres par titre, auteur ou ISBN
- Voir la disponibilité en temps réel
- Marquer les livres comme disponibles ou empruntés

![Gestion des livres](img/4png)

### Gestion des Utilisateurs
- Création de comptes utilisateurs (membres et administrateurs)
- Authentification sécurisée avec hashage des mots de passe
- Profils utilisateurs avec historique d'emprunts
- Gestion des rôles (admin/membre)

![Gestion des utilisateurs](img/5png)

### Système d'Emprunts
- Emprunter des livres avec date d'échéance
- Retourner des livres
- Suivi des emprunts en cours
- Alertes pour les retards
- Historique complet des emprunts

![Gestion des emprunts](img/6.png)

### Réservations
- Réserver des livres indisponibles
- File d'attente des réservations
- Notifications quand un livre devient disponible
- Annulation de réservations

![Gestion des réservations](img/7.png)

### Connexion et Authentification
- Interface de connexion sécurisée
- Gestion des sessions utilisateur
- Inscription de nouveaux membres

![Page de connexion](img/1.png)

### Interface d'Administration
- Tableau de bord complet
- Statistiques en temps réel
- Gestion centralisée de toutes les fonctionnalités

![Interface d'administration](img/3.png)

## 🛠️ Technologies Utilisées

- **Backend**: Flask (Python)
- **Base de données**: PostgreSQL 16 / SQLite
- **ORM**: SQLAlchemy
- **Conteneurisation**: Podman
- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **Authentification**: Flask Sessions avec hashage bcrypt

## 📋 Prérequis

- Python 3.11+
- Podman Desktop (ou Docker)
- Git

## 🚀 Installation et Déploiement

### 1. Cloner le projet

```bash
git clone https://github.com/sarahlouazzani/GestionBiblio.git
cd GestionBiblio
```

### 2. Installer les dépendances Python

```bash
pip install -r requirements.txt
```

Si le fichier `requirements.txt` n'existe pas, installez manuellement :

```bash
pip install flask flask-sqlalchemy psycopg2-binary
```

### 3. Configuration de la base de données avec Podman

#### Option A : Démarrage automatique (Windows)

```powershell
.\start.ps1
```

#### Option B : Démarrage manuel

**Sur Windows PowerShell :**
```powershell
# Créer et démarrer le conteneur PostgreSQL
podman run -d `
  --name postgres-gestionbiblio `
  --tls-verify=false `
  -e POSTGRES_USER=sarah `
  -e POSTGRES_PASSWORD=sarah123 `
  -e POSTGRES_DB=gestionbiblio `
  -e POSTGRES_HOST_AUTH_METHOD=trust `
  -p 5432:5432 `
  postgres:16
```

**Sur Linux/Mac :**
```bash
# Créer et démarrer le conteneur PostgreSQL
podman run -d \
  --name postgres-gestionbiblio \
  -e POSTGRES_USER=sarah \
  -e POSTGRES_PASSWORD=sarah123 \
  -e POSTGRES_DB=gestionbiblio \
  -e POSTGRES_HOST_AUTH_METHOD=trust \
  -p 5432:5432 \
  postgres:16
```

#### Vérifier que le conteneur fonctionne

```bash
podman ps
```

Vous devriez voir `postgres-gestionbiblio` dans la liste.

### 4. Initialiser la base de données

```bash
python -c "from app import create_app, db; app = create_app(); ctx = app.app_context(); ctx.push(); db.create_all(); print('Base de données initialisée'); ctx.pop()"
```

### 5. Remplir la base avec des données de test (optionnel)

```bash
python seed_data.py
```

Cela créera :
- 6 utilisateurs (2 admins, 4 membres)
- 20 livres
- 5 emprunts
- 4 réservations

### 6. Lancer l'application

```bash
python run.py
```

L'application sera accessible sur : **http://127.0.0.1:5000**

## 🔐 Identifiants par défaut

Après avoir exécuté `seed_data.py` :

- **Email** : `admin@biblio.fr`
- **Mot de passe** : `password123`

Tous les utilisateurs de test utilisent le mot de passe : `password123`

## 📁 Structure du Projet

```
gestionbiblio/
├── app/
│   ├── __init__.py              # Initialisation de l'application Flask
│   ├── config.py                # Configuration de la base de données
│   ├── models/                  # Modèles de données (ORM)
│   │   ├── books.py             # Modèle Livre
│   │   ├── users.py             # Modèle Utilisateur
│   │   ├── loans.py             # Modèle Emprunt
│   │   └── reservations.py     # Modèle Réservation
│   ├── routes/                  # Routes/API Flask
│   │   ├── books_routes.py      # Routes pour les livres
│   │   ├── users_routes.py      # Routes pour les utilisateurs
│   │   ├── loans_routes.py      # Routes pour les emprunts
│   │   └── reservations_routes.py # Routes pour les réservations
│   └── templates/               # Templates HTML
│       ├── base.html            # Template de base
│       ├── home.html            # Page d'accueil
│       ├── login.html           # Page de connexion
│       ├── books.html           # Gestion des livres
│       ├── users.html           # Gestion des utilisateurs
│       ├── loans.html           # Gestion des emprunts
│       └── reservations.html   # Gestion des réservations
├── instance/                    # Base de données SQLite (si utilisée)
├── migrations/                  # Migrations de base de données
├── img/                         # Captures d'écran
├── run.py                       # Point d'entrée de l'application
├── seed_data.py                 # Script de remplissage de données
├── start.ps1                    # Script de démarrage Windows
└── README.md                    # Ce fichier
```

## 🔄 Commandes Podman Utiles

### Démarrer le conteneur existant
```bash
podman start postgres-gestionbiblio
```

### Arrêter le conteneur
```bash
podman stop postgres-gestionbiblio
```

### Voir les logs
```bash
podman logs postgres-gestionbiblio
```

### Accéder au shell PostgreSQL
```bash
podman exec -it postgres-gestionbiblio psql -U sarah -d gestionbiblio
```

### Supprimer le conteneur
```bash
podman stop postgres-gestionbiblio
podman rm postgres-gestionbiblio
```

### Nettoyer tous les conteneurs et images
```bash
podman system prune -a -f --volumes
```

## 🌐 Déploiement sur une Autre Machine

### 1. Installer Podman

**Windows :**
- Télécharger et installer [Podman Desktop](https://podman-desktop.io/)

**Linux :**
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install podman

# Fedora/RHEL
sudo dnf install podman
```

**macOS :**
```bash
brew install podman
podman machine init
podman machine start
```

### 2. Cloner et Configurer

```bash
# Cloner le projet
git clone https://github.com/sarahlouazzani/GestionBiblio.git
cd GestionBiblio

# Installer Python et les dépendances
pip install -r requirements.txt

# Démarrer PostgreSQL avec Podman
podman run -d \
  --name postgres-gestionbiblio \
  -e POSTGRES_USER=sarah \
  -e POSTGRES_PASSWORD=sarah123 \
  -e POSTGRES_DB=gestionbiblio \
  -p 5432:5432 \
  postgres:16

# Attendre 5 secondes que PostgreSQL démarre
sleep 5

# Initialiser la base de données
python -c "from app import create_app, db; app = create_app(); ctx = app.app_context(); ctx.push(); db.create_all(); ctx.pop()"

# Remplir avec des données de test (optionnel)
python seed_data.py

# Lancer l'application
python run.py
```

### 3. Configuration pour Production

Pour un environnement de production, modifiez `app/config.py` :

```python
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        "postgresql://sarah:sarah123@localhost:5432/gestionbiblio"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'votre-clé-secrète-très-sécurisée'
```

Utilisez des variables d'environnement pour les informations sensibles :

```bash
export SECRET_KEY="votre-clé-secrète-aléatoire"
export DATABASE_URL="postgresql://user:password@host:5432/dbname"
```

## 🐛 Dépannage

### Le conteneur PostgreSQL ne démarre pas

```bash
# Vérifier les logs
podman logs postgres-gestionbiblio

# Redémarrer le conteneur
podman restart postgres-gestionbiblio
```

### Erreur de connexion à la base de données

1. Vérifiez que le conteneur est en cours d'exécution :
   ```bash
   podman ps
   ```

2. Vérifiez que le port 5432 est bien mappé :
   ```bash
   podman port postgres-gestionbiblio
   ```

3. Testez la connexion :
   ```bash
   podman exec postgres-gestionbiblio psql -U sarah -d gestionbiblio -c "SELECT version();"
   ```

### L'application ne démarre pas

1. Vérifiez les dépendances Python :
   ```bash
   pip list | grep -E "flask|sqlalchemy|psycopg2"
   ```

2. Vérifiez les erreurs dans la console

3. Réinitialisez la base de données :
   ```bash
   python -c "from app import create_app, db; app = create_app(); ctx = app.app_context(); ctx.push(); db.drop_all(); db.create_all(); ctx.pop()"
   ```

## 📝 API Endpoints

### Utilisateurs
- `POST /users/register` - Inscription
- `POST /users/login` - Connexion
- `POST /users/logout` - Déconnexion
- `GET /users/` - Liste des utilisateurs
- `POST /users/` - Ajouter un utilisateur
- `PUT /users/<id>` - Modifier un utilisateur
- `DELETE /users/<id>` - Supprimer un utilisateur

### Livres
- `GET /books/` - Liste des livres
- `POST /books/` - Ajouter un livre
- `PUT /books/<id>` - Modifier un livre
- `DELETE /books/<id>` - Supprimer un livre

### Emprunts
- `GET /loans/` - Liste des emprunts
- `POST /loans/` - Créer un emprunt
- `PUT /loans/<id>/return` - Retourner un livre

### Réservations
- `GET /reservations/` - Liste des réservations
- `POST /reservations/` - Créer une réservation
- `PUT /reservations/<id>` - Modifier une réservation
- `DELETE /reservations/<id>` - Annuler une réservation

## 👥 Auteurs

- **Sarah Louazzani** - [GitHub](https://github.com/sarahlouazzani)

## 📄 Licence

Ce projet est sous licence MIT.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

1. Fork le projet
2. Créez votre branche (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📞 Support

Pour toute question ou problème, ouvrez une issue sur GitHub.
