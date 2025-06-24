# E-Boutique Django

E-Boutique est une application web développée avec Django permettant la gestion d'une boutique en ligne : publication d'articles, gestion de panier, commandes, profils utilisateurs, et paiements par carte de crédit. L'interface utilise Bootstrap pour un rendu moderne et responsive.

## Fonctionnalités principales
- Authentification et inscription des utilisateurs
- Gestion des profils utilisateurs (photo, informations personnelles)
- Ajout, modification, suppression et publication d'articles
- Gestion du panier d'achat
- Passage et suivi des commandes
- Paiement par carte de crédit (simulation)
- Tableau de bord utilisateur et superutilisateur
- Recherche d'articles
- Messagerie interne (messages entre utilisateurs)
- Pages d'information : À propos, Contact

## Prérequis
- Python 3.x
- Django 5.x
- (Optionnel) Environnement virtuel Python

## Installation
1. **Cloner le dépôt**
2. **Installer les dépendances** :
   ```bash
   pip install django pillow
   ```
3. **Appliquer les migrations** :
   ```bash
   python manage.py migrate
   ```
4. **Créer un superutilisateur** :
   ```bash
   python manage.py createsuperuser
   ```
   Par défaut (voir `guide.txt`) :
   - username: `@EboutiqueSuperAdim@`
   - mot de passe: `1234`
5. **Lancer le serveur de développement** :
   ```bash
   python manage.py runserver
   ```

## Structure du projet
- `eboutique/models.py` :
  - **Article** : gestion des articles (titre, auteur, image, contenu, type, prix, stock...)
  - **Message** : messagerie interne
  - **Cart_de_credit** : gestion des cartes de crédit
  - **Transaction** : historique des transactions
  - **mon_panier** : panier utilisateur
  - **Commande** : gestion des commandes
  - **user_profil** : profil utilisateur (photo, infos)
- `eboutique/views.py` : toutes les vues (logique métier)
- `eboutique/templates/eboutique/` : templates HTML (Bootstrap)
- `eboutique/static/eboutique/` : fichiers statiques (CSS, JS, images)
- `MonProjet/settings.py` : configuration Django
- `manage.py` : gestionnaire de commandes Django
- `guide.txt` : guide rapide d'utilisation

## Utilisation
- Accès à l'interface via `http://localhost:8000/`
- Inscription, connexion, gestion du profil
- Ajout d'articles, gestion du panier, passage de commande
- Ajout d'une carte de crédit (simulation)
- Tableau de bord pour suivre ses commandes et articles
- Recherche et filtrage d'articles

## Commandes utiles
- Lancer le serveur :
  ```bash
  python manage.py runserver
  ```
- Créer un superutilisateur :
  ```bash
  python manage.py createsuperuser
  ```
- Appliquer les migrations :
  ```bash
  python manage.py migrate
  ```

---

*Projet réalisé dans le cadre d'un projet de boutique en ligne avec gestion complète des utilisateurs, articles, commandes et paiements.* 


##Support

Pour toute question ou problème, veuillez   me  contacter par mail billaassouma@188gmail.com ou +229 53400160.
