Excellent 👏 tu veux **apprendre en construisant** — c’est la meilleure approche.
Je vais agir comme **un instructeur technique**, et t’aider à **structurer ton apprentissage sur la phase 1 (Backend / Django REST Framework)** avec un **projet concret et guidé**.

---

## 🧭 Objectif global de la Phase 1

> Créer une **API REST complète** (produits & catégories) en suivant les bonnes pratiques pro (structure, tests, Docker, doc).

Tu vas apprendre à :

- Monter un environnement professionnel
- Concevoir des modèles clairs
- Créer une API REST propre avec Django + DRF
- Gérer l’authentification et les permissions
- Conteneuriser ton app avec Docker
- Documenter comme un vrai projet pro

---

## 🏗️ Projet fil conducteur : **“Mini catalogue de produits”**

Ce projet va te servir de **base d’apprentissage**.
👉 Il contiendra :

- des **catégories** (ex : Électronique, Mode, Maison)
- des **produits** (nom, prix, description, catégorie)
- des **utilisateurs** (staff / normal)
- un **système d’API REST sécurisée**

---

## 📆 Semaine 1 — Setup pro & bases DRF

### 🎯 Objectif pédagogique :

Mettre en place un environnement Django pro et construire la première API REST basique.

---

### 🧩 Étape 1 — Installation et préparation de l’environnement

1. **Installer Python et Docker**

   ```bash
   python --version
   docker --version
   ```

   > Si Docker n’est pas installé, télécharge depuis [docker.com](https://www.docker.com/products/docker-desktop).

2. **Créer ton environnement virtuel**

   ```bash
   python -m venv venv
   source venv/Scripts/activate  # (Windows)
   source venv/bin/activate      # (Linux/Mac)
   ```

3. **Installer Django et DRF**

   ```bash
   pip install django djangorestframework psycopg2-binary
   ```

4. **Créer ton projet Django**

   ```bash
   django-admin startproject catalog_api
   cd catalog_api
   python manage.py startapp products
   ```

---

### 🧩 Étape 2 — Structuration du code

Voici la structure à viser :

```
catalog_api/
│
├── catalog_api/          # Configuration principale
│   ├── settings.py
│   ├── urls.py
│
├── products/             # Ton app principale
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── manage.py
└── requirements.txt
```

> 💡 **Bon réflexe :** dès maintenant, crée un fichier `requirements.txt` :

```bash
pip freeze > requirements.txt
```

---

### 🧩 Étape 3 — Créer les modèles

Dans `products/models.py` :

```python
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return self.name
```

Applique les migrations :

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 🧩 Étape 4 — Créer les serializers

`products/serializers.py` :

```python
from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'category', 'category_name']
```

---

### 🧩 Étape 5 — Créer les vues API

`products/views.py` :

```python
from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

---

### 🧩 Étape 6 — Configurer les routes

`products/urls.py` :

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

Et dans `catalog_api/urls.py` :

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
]
```

---

### 🧩 Étape 7 — Lancer le serveur et tester

```bash
python manage.py runserver
```

Teste sur :
👉 `http://127.0.0.1:8000/api/categories/`
👉 `http://127.0.0.1:8000/api/products/`

---

### 🧩 Étape 8 — Rédiger le README.md

Crée un fichier `README.md` à la racine :

````markdown
# 🛍️ Catalog API

API REST pour gérer des catégories et produits.

## 🚀 Installation

1. Cloner le repo
2. Créer un environnement virtuel
3. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
````

4. Lancer le serveur :

   ```bash
   python manage.py runserver
   ```

## 🔗 Endpoints

- `/api/categories/`
- `/api/products/`

```

---

### ✅ Résultat attendu fin de semaine 1 :
- API Django propre fonctionnelle
- CRUD complet pour Category et Product
- README clair et structuré
- Structure de projet pro

---

Souhaites-tu que je te fasse la **même feuille d’instructions** pour la **Semaine 2 (Bonnes pratiques DRF)** — avec JWT, permissions et tests ?
Cela te donnera un **plan d’exécution semaine par semaine** pour progresser comme un vrai dev backend.
```
