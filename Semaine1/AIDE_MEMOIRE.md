# 🔧 AIDE-MÉMOIRE - COMMANDES UTILES

## 🚀 DÉMARRAGE

```powershell
# Activer l'environnement virtuel
cd "c:\Users\wwwad\PycharmProjects\FULL STACK DEV"
venv\Scripts\activate

# Aller dans le projet
cd Semaine1\testmodels

# Installer les dépendances
pip install -r requirements_API.txt

# Migrations
python manage.py makemigrations
python manage.py migrate

# Créer un superuser
python manage.py createsuperuser

# Lancer le serveur
python manage.py runserver
```

---

## 📝 EXEMPLES DE REQUÊTES

### CATEGORY

#### Lister toutes les catégories

```bash
curl http://localhost:8000/api/categories/
```

#### Créer une catégorie

```bash
curl -X POST http://localhost:8000/api/categories/ ^
  -H "Content-Type: application/json" ^
  -d "{\"name\": \"Électronique\", \"description\": \"Produits électroniques\"}"
```

#### Obtenir une catégorie

```bash
curl http://localhost:8000/api/categories/1/
```

#### Modifier une catégorie (PATCH)

```bash
curl -X PATCH http://localhost:8000/api/categories/1/ ^
  -H "Content-Type: application/json" ^
  -d "{\"description\": \"Nouvelle description\"}"
```

#### Supprimer une catégorie

```bash
curl -X DELETE http://localhost:8000/api/categories/1/
```

#### Rechercher des catégories

```bash
curl "http://localhost:8000/api/categories/?search=électronique"
```

#### Trier les catégories

```bash
curl "http://localhost:8000/api/categories/?ordering=name"
```

---

### PRODUCT

#### Créer un produit

```bash
curl -X POST http://localhost:8000/api/products/ ^
  -H "Content-Type: application/json" ^
  -d "{\"name\": \"Smartphone\", \"price\": \"599.99\", \"description\": \"Un super smartphone\", \"category\": 1, \"stock\": 10, \"suppliers\": [1, 2]}"
```

#### Filtrer par catégorie

```bash
curl "http://localhost:8000/api/products/?category=1"
```

#### Produits en rupture de stock (action personnalisée)

```bash
curl http://localhost:8000/api/products/low_stock/
```

#### Avis d'un produit (action personnalisée)

```bash
curl http://localhost:8000/api/products/1/reviews/
```

---

### ORDER

#### Créer une commande

```bash
curl -X POST http://localhost:8000/api/orders/ ^
  -H "Content-Type: application/json" ^
  -H "Authorization: Basic dXNlcjpwYXNz" ^
  -d "{\"client\": 1, \"status\": \"Pending\"}"
```

#### Mes commandes (action personnalisée)

```bash
curl -H "Authorization: Basic dXNlcjpwYXNz" ^
  http://localhost:8000/api/orders/my_orders/
```

#### Confirmer une commande (action personnalisée)

```bash
curl -X POST ^
  -H "Authorization: Basic dXNlcjpwYXNz" ^
  http://localhost:8000/api/orders/UUID/confirm/
```

---

### REVIEW

#### Créer un avis

```bash
curl -X POST http://localhost:8000/api/reviews/ ^
  -H "Content-Type: application/json" ^
  -H "Authorization: Basic dXNlcjpwYXNz" ^
  -d "{\"product\": 1, \"rating\": 5, \"comment\": \"Excellent produit, je recommande vivement!\"}"
```

#### Meilleurs avis (action personnalisée)

```bash
curl http://localhost:8000/api/reviews/top_rated/
```

---

## 🐍 EXEMPLES PYTHON

### Utiliser l'API avec requests

```python
import requests

BASE_URL = "http://localhost:8000/api"

# GET - Lister
response = requests.get(f"{BASE_URL}/categories/")
print(response.json())

# POST - Créer
data = {
    "name": "Livres",
    "description": "Livres et magazines"
}
response = requests.post(f"{BASE_URL}/categories/", json=data)
print(response.json())

# GET - Détail
response = requests.get(f"{BASE_URL}/categories/1/")
print(response.json())

# PATCH - Modifier
data = {"description": "Nouvelle description"}
response = requests.patch(f"{BASE_URL}/categories/1/", json=data)
print(response.json())

# DELETE - Supprimer
response = requests.delete(f"{BASE_URL}/categories/1/")
print(response.status_code)  # 204 = succès
```

### Avec authentification

```python
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('username', 'password')

# Créer un avis (authentification requise)
data = {
    "product": 1,
    "rating": 5,
    "comment": "Excellent produit!"
}
response = requests.post(
    "http://localhost:8000/api/reviews/",
    json=data,
    auth=auth
)
print(response.json())
```

---

## 🧪 TESTS

### Lancer tous les tests

```powershell
python manage.py test
```

### Lancer les tests d'une app

```powershell
python manage.py test app
```

### Lancer les tests d'une classe

```powershell
python manage.py test app.tests_EXERCICES.CategoryAPITestCase
```

### Lancer un test spécifique

```powershell
python manage.py test app.tests_EXERCICES.CategoryAPITestCase.test_create_category
```

### Avec verbosité

```powershell
python manage.py test --verbosity=2
```

### Avec couverture de code

```powershell
# Installer coverage
pip install coverage

# Lancer les tests avec coverage
coverage run --source='.' manage.py test

# Voir le rapport dans le terminal
coverage report

# Générer un rapport HTML
coverage html
# Ouvrir htmlcov/index.html dans un navigateur
```

---

## 🗄️ BASE DE DONNÉES

### Créer des migrations

```powershell
python manage.py makemigrations
```

### Appliquer les migrations

```powershell
python manage.py migrate
```

### Afficher les migrations

```powershell
python manage.py showmigrations
```

### Shell Django

```powershell
python manage.py shell
```

Puis dans le shell :

```python
from app.models import Category, Product

# Créer une catégorie
cat = Category.objects.create(name="Test", description="Description")

# Lister toutes les catégories
Category.objects.all()

# Filtrer
Category.objects.filter(name__icontains="électronique")

# Obtenir une catégorie
cat = Category.objects.get(id=1)

# Accéder aux produits de la catégorie
cat.products.all()
```

---

## 📊 DONNÉES DE TEST

### Script Python pour créer des données

Créer un fichier `populate_db.py` :

```python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testmodels.settings')
django.setup()

from app.models import Category, Supplier, Client, Product
from django.contrib.auth.models import User

# Créer des catégories
cat1 = Category.objects.create(name="Électronique", description="Produits électroniques")
cat2 = Category.objects.create(name="Vêtements", description="Vêtements et accessoires")
cat3 = Category.objects.create(name="Livres", description="Livres et magazines")

# Créer des fournisseurs
sup1 = Supplier.objects.create(
    name="TechSupply",
    contact_name="Jean Dupont",
    email="jean@techsupply.com",
    phone_number="0123456789"
)
sup2 = Supplier.objects.create(
    name="GlobalTrade",
    contact_name="Marie Martin",
    email="marie@globaltrade.com"
)

# Créer des clients
client1 = Client.objects.create(
    first_name="Pierre",
    last_name="Durand",
    email="pierre@example.com",
    phone_number="0612345678"
)

# Créer un utilisateur
user = User.objects.create_user(
    username='testuser',
    email='test@example.com',
    password='testpass123'
)

# Créer des produits
prod1 = Product.objects.create(
    name="Smartphone XYZ",
    price=599.99,
    description="Un excellent smartphone avec toutes les fonctionnalités modernes",
    category=cat1,
    stock=50
)
prod1.supplier.add(sup1, sup2)

prod2 = Product.objects.create(
    name="Laptop Pro",
    price=1299.99,
    description="Un laptop puissant pour les professionnels",
    category=cat1,
    stock=20
)
prod2.supplier.add(sup1)

prod3 = Product.objects.create(
    name="T-Shirt Premium",
    price=29.99,
    description="Un t-shirt de qualité supérieure en coton bio",
    category=cat2,
    stock=100
)
prod3.supplier.add(sup2)

print("✅ Base de données peuplée avec succès!")
print(f"- {Category.objects.count()} catégories")
print(f"- {Supplier.objects.count()} fournisseurs")
print(f"- {Client.objects.count()} clients")
print(f"- {Product.objects.count()} produits")
print(f"- {User.objects.count()} utilisateurs")
```

Lancer le script :

```powershell
python populate_db.py
```

---

## 🔍 DEBUGGING

### Vérifier les URLs

```powershell
python manage.py show_urls
```

### Vérifier la configuration

```powershell
python manage.py check
```

### Shell interactif

```powershell
python manage.py shell
```

### Voir les requêtes SQL

Dans `settings.py`, ajouter :

```python
LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
```

---

## 📦 GESTION DES DÉPENDANCES

### Voir les packages installés

```powershell
pip list
```

### Créer un fichier requirements

```powershell
pip freeze > requirements.txt
```

### Installer depuis requirements

```powershell
pip install -r requirements.txt
```

### Mettre à jour un package

```powershell
pip install --upgrade django
```

---

## 🌐 URLS UTILES

- **API Root:** http://localhost:8000/api/
- **Admin:** http://localhost:8000/admin/
- **Swagger UI:** http://localhost:8000/swagger/
- **ReDoc:** http://localhost:8000/redoc/
- **Schema JSON:** http://localhost:8000/swagger.json

---

## 💡 ASTUCES

### Activer l'auto-reload

Le serveur Django recharge automatiquement quand vous modifiez des fichiers Python.

### Utiliser ipython pour le shell

```powershell
pip install ipython
python manage.py shell
# Vous aurez un shell plus convivial avec coloration syntaxique
```

### Django Debug Toolbar

```powershell
pip install django-debug-toolbar
```

Puis configurer dans `settings.py` pour voir les requêtes SQL, le temps d'exécution, etc.

---

**Bon développement ! 🚀**
