# 📖 README - EXERCICES API DJANGO REST FRAMEWORK

## 🎯 OBJECTIF

Apprendre à créer une **API REST professionnelle complète** avec Django REST Framework en travaillant sur un projet réel de boutique en ligne.

---

## 📂 STRUCTURE DES FICHIERS

```
Semaine1/
├── GUIDE_API_EXERCISES.md          # 📚 Guide pédagogique principal
├── PLAN_ACTION.md                  # 📅 Planning sur 5 jours
├── testmodels/
│   ├── app/
│   │   ├── models.py               # ✅ Modèles (déjà fait)
│   │   ├── serializers_EXERCICES.py # ✍️ À compléter (21 serializers)
│   │   ├── views_EXERCICES.py      # ✍️ À compléter (7 ViewSets + 10 actions)
│   │   ├── tests_EXERCICES.py      # ✍️ À compléter (25+ tests)
│   ├── testmodels/
│   │   ├── urls_EXERCICES.py       # ✍️ À compléter (routing)
│   │   ├── CONFIGURATION_DRF.py    # ⚙️ Configuration à copier dans settings.py
│   ├── requirements_API.txt        # 📦 Dépendances à installer
```

---

## 🚀 DÉMARRAGE RAPIDE

### 1️⃣ Installation

```bash
# Activer votre environnement virtuel
cd "c:\Users\wwwad\PycharmProjects\FULL STACK DEV"
venv\Scripts\activate

# Installer les dépendances
cd Semaine1\testmodels
pip install -r requirements_API.txt
```

### 2️⃣ Configuration

Ouvrir `testmodels/settings.py` et ajouter la configuration de `CONFIGURATION_DRF.py`

### 3️⃣ Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ Créer un superuser

```bash
python manage.py createsuperuser
```

### 5️⃣ Lancer le serveur

```bash
python manage.py runserver
```

### 6️⃣ Tester

Visitez :

- http://localhost:8000/api/ (Browsable API)
- http://localhost:8000/swagger/ (Documentation Swagger)
- http://localhost:8000/admin/ (Admin Django)

---

## 📚 ORDRE DE LECTURE

1. **GUIDE_API_EXERCISES.md** - Comprendre les concepts
2. **PLAN_ACTION.md** - Suivre le planning jour par jour
3. **serializers_EXERCICES.py** - Commencer par les serializers
4. **views_EXERCICES.py** - Puis les vues
5. **urls_EXERCICES.py** - Configurer les URLs
6. **tests_EXERCICES.py** - Écrire les tests

---

## ✍️ EXERCICES À RÉALISER

### 📊 Résumé

| Type                       | À faire                  | Difficulté      | Temps estimé |
| -------------------------- | ------------------------ | --------------- | ------------ |
| **Serializers**            | 18 (3 par modèle × 6)    | Moyenne         | 3-4h         |
| **ViewSets**               | 6                        | Moyenne         | 4-5h         |
| **Actions personnalisées** | 10                       | Moyenne-Avancée | 2-3h         |
| **URLs**                   | Configuration du routing | Facile          | 30 min       |
| **Tests**                  | 25+ tests                | Moyenne         | 3-4h         |
| **TOTAL**                  |                          |                 | **13-17h**   |

### 📝 Détail par modèle

#### 1. Category (✅ EXEMPLE COMPLET - À ÉTUDIER)

- ✅ CategoryCreateSerializer
- ✅ CategoryListSerializer
- ✅ CategoryDetailSerializer
- ✅ CategoryViewSet
- ✅ 2 actions personnalisées

#### 2. Supplier (❌ À FAIRE)

- ⬜ SupplierCreateSerializer
- ⬜ SupplierListSerializer
- ⬜ SupplierDetailSerializer
- ⬜ SupplierViewSet
- ⬜ 1 action personnalisée

#### 3. Client (❌ À FAIRE)

- ⬜ ClientCreateSerializer
- ⬜ ClientListSerializer
- ⬜ ClientDetailSerializer
- ⬜ ClientViewSet
- ⬜ 1 action personnalisée

#### 4. Product (❌ À FAIRE - LE PLUS IMPORTANT)

- ⬜ ProductCreateSerializer
- ⬜ ProductListSerializer
- ⬜ ProductDetailSerializer
- ⬜ ProductViewSet
- ⬜ 3 actions personnalisées

#### 5. Review (❌ À FAIRE)

- ⬜ ReviewCreateSerializer
- ⬜ ReviewListSerializer
- ⬜ ReviewDetailSerializer
- ⬜ ReviewViewSet
- ⬜ 1 action personnalisée

#### 6. Order (❌ À FAIRE - NIVEAU AVANCÉ)

- ⬜ OrderCreateSerializer
- ⬜ OrderListSerializer
- ⬜ OrderDetailSerializer
- ⬜ OrderViewSet
- ⬜ 4 actions personnalisées

#### 7. OrderItem (❌ À FAIRE)

- ⬜ OrderItemCreateSerializer
- ⬜ OrderItemListSerializer
- ⬜ OrderItemDetailSerializer
- ⬜ OrderItemViewSet

---

## 🎓 COMPÉTENCES ACQUISES

Après avoir terminé ces exercices, vous saurez :

### ✅ Serializers

- Créer des serializers pour la création (write)
- Créer des serializers pour la lecture (read)
- Gérer les relations (ForeignKey, ManyToMany)
- Créer des validations personnalisées
- Utiliser SerializerMethodField
- Calculer des champs dynamiques

### ✅ Views

- Utiliser ModelViewSet pour le CRUD complet
- Choisir le bon serializer selon l'action
- Optimiser les requêtes (select_related, prefetch_related)
- Créer des actions personnalisées (@action)
- Gérer les filtres et la recherche
- Implémenter la pagination

### ✅ URLs

- Configurer un Router
- Créer une structure d'URLs RESTful
- Documenter l'API avec Swagger

### ✅ Tests

- Écrire des tests unitaires pour les APIs
- Tester les validations
- Tester les relations
- Calculer la couverture de code

---

## 🧪 TESTER VOTRE API

### Avec le navigateur

```
http://localhost:8000/api/categories/
```

### Avec curl

```bash
# GET
curl http://localhost:8000/api/categories/

# POST
curl -X POST http://localhost:8000/api/categories/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Test", "description": "Description"}'
```

### Avec Python

```python
import requests

response = requests.get('http://localhost:8000/api/categories/')
print(response.json())
```

### Avec Postman

Importer la collection depuis Swagger : http://localhost:8000/swagger.json

---

## 📊 PROGRESSION

### Jour 1 : Configuration + Modèles simples

- ⬜ Configuration de l'environnement
- ⬜ Supplier (3 serializers + ViewSet)
- ⬜ Client (3 serializers + ViewSet)

### Jour 2 : Modèles avec relations

- ⬜ Product (3 serializers + ViewSet + 3 actions)

### Jour 3 : Avis

- ⬜ Review (3 serializers + ViewSet + 1 action)

### Jour 4 : Commandes

- ⬜ Order (3 serializers + ViewSet + 4 actions)

### Jour 5 : OrderItems + Tests

- ⬜ OrderItem (3 serializers + ViewSet)
- ⬜ Tests unitaires (25+ tests)

---

## 🏆 CRITÈRES DE RÉUSSITE

- ✅ Tous les serializers créés (21)
- ✅ Tous les ViewSets créés (7)
- ✅ Toutes les actions créées (10)
- ✅ Tous les tests passent
- ✅ Couverture de code > 80%
- ✅ Documentation Swagger fonctionnelle
- ✅ API complètement fonctionnelle

---

## 💡 CONSEILS

1. **Commencez simple** : Category est votre référence
2. **Testez au fur et à mesure** : Ne passez pas au suivant avant que le précédent fonctionne
3. **Lisez la documentation** : Django REST Framework est très bien documenté
4. **Utilisez le browsable API** : C'est un outil puissant pour tester
5. **Écrivez des tests** : Ça vous aide à comprendre et à valider votre code

---

## 🆘 EN CAS DE PROBLÈME

### Erreur d'import

```bash
pip install -r requirements_API.txt
```

### Erreur de migration

```bash
python manage.py makemigrations
python manage.py migrate
```

### Serveur ne démarre pas

Vérifier que le port 8000 n'est pas déjà utilisé

### Tests échouent

Lire attentivement le message d'erreur et vérifier la logique

---

## 📚 RESSOURCES

- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django Documentation](https://docs.djangoproject.com/)
- [drf-yasg](https://drf-yasg.readthedocs.io/)

---

## 🎉 FÉLICITATIONS !

Une fois terminé, vous aurez créé une **API REST complète** avec :

- **40+ endpoints**
- **7 modèles** interconnectés
- **21 serializers**
- **10 actions personnalisées**
- **25+ tests unitaires**
- **Documentation automatique**

C'est un projet impressionnant pour votre portfolio ! 🚀

---

**Bon courage et amusez-vous bien ! 💪**
