# 🎓 GUIDE PÉDAGOGIQUE - CRÉATION D'API REST AVEC DJANGO REST FRAMEWORK

## 📋 OBJECTIFS D'APPRENTISSAGE

Vous allez apprendre à créer une API REST complète et professionnelle en suivant les meilleures pratiques Django.

---

## 🏗️ ARCHITECTURE DE VOTRE PROJET

Vous avez 6 modèles interconnectés :

1. **Category** - Catégories de produits
2. **Product** - Produits (avec relations vers Category et Supplier)
3. **Order** - Commandes (avec UUID comme clé primaire)
4. **OrderItem** - Articles de commande (table intermédiaire)
5. **Review** - Avis sur les produits
6. **Client** - Clients de la boutique
7. **Supplier** - Fournisseurs

---

## 📝 EXERCICE 1 : SERIALIZERS (OBLIGATOIRE)

### CONSIGNES :

Pour chaque modèle, vous devez créer **3 types de serializers** :

#### A) Serializer de CRÉATION (Write)

- **Objectif** : Accepter les données en entrée pour créer un objet
- **Règles** :
  - Tous les champs requis doivent être présents
  - Les relations doivent accepter des IDs (pas des objets complets)
  - Ajouter des validations personnalisées

#### B) Serializer de LISTE (Read - Simple)

- **Objectif** : Retourner une liste légère d'objets
- **Règles** :
  - Seulement les champs essentiels
  - Pas de relations imbriquées (juste les IDs ou noms)
  - Optimisé pour la performance

#### C) Serializer de DÉTAIL (Read - Complet)

- **Objectif** : Retourner tous les détails d'un objet
- **Règles** :
  - Tous les champs importants
  - Relations imbriquées complètes
  - Champs calculés (SerializerMethodField)

---

## 🎯 EXERCICE 2 : VIEWS (OBLIGATOIRE)

### TYPES DE VUES À IMPLÉMENTER :

#### Pour TOUS les modèles, créer :

1. **ListView** - GET /api/model/ (liste)
2. **CreateView** - POST /api/model/ (création)
3. **RetrieveView** - GET /api/model/{id}/ (détail)
4. **UpdateView** - PUT/PATCH /api/model/{id}/ (modification)
5. **DestroyView** - DELETE /api/model/{id}/ (suppression)

#### OU utiliser ViewSets (niveau avancé) :

- **ModelViewSet** : Combine toutes les opérations CRUD

### RÈGLES OBLIGATOIRES :

- ✅ Utiliser le bon serializer selon l'action
- ✅ Ajouter des filtres (filter_backends)
- ✅ Ajouter la pagination
- ✅ Ajouter des permissions
- ✅ Gérer les erreurs proprement

---

## 🔗 EXERCICE 3 : URLS (OBLIGATOIRE)

### CHOIX D'ARCHITECTURE :

#### Option 1 : URLs explicites (débutant)

```python
urlpatterns = [
    path('api/products/', ProductListView.as_view()),
    path('api/products/<int:pk>/', ProductDetailView.as_view()),
    path('api/products/create/', ProductCreateView.as_view()),
]
```

#### Option 2 : Router avec ViewSets (recommandé)

```python
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
urlpatterns = router.urls
```

### STRUCTURE OBLIGATOIRE :

```
/api/
  /categories/
  /products/
  /orders/
  /order-items/
  /reviews/
  /clients/
  /suppliers/
```

---

## 🎨 EXERCICE 4 : FONCTIONNALITÉS AVANCÉES (BONUS)

### A) Filtrage

- Filtrer les produits par catégorie
- Filtrer les commandes par statut
- Recherche par nom

### B) Actions personnalisées

```python
@action(detail=True, methods=['post'])
def confirm_order(self, request, pk=None):
    # Confirmer une commande
    pass

@action(detail=False, methods=['get'])
def low_stock(self, request):
    # Produits en rupture de stock
    pass
```

### C) Champs calculés

- Prix total d'une commande
- Moyenne des notes (reviews)
- Nombre de produits par catégorie

---

## ✅ CHECKLIST DE VALIDATION

Avant de considérer votre API complète, vérifiez :

### Serializers

- [ ] Tous les modèles ont leurs 3 serializers
- [ ] Les validations personnalisées fonctionnent
- [ ] Les relations sont bien gérées

### Views

- [ ] CRUD complet pour chaque modèle
- [ ] Pagination activée
- [ ] Filtres fonctionnels

### URLs

- [ ] Structure logique et cohérente
- [ ] Noms de routes explicites
- [ ] Documentation automatique accessible

### Tests

- [ ] Tester la création d'objets
- [ ] Tester les validations
- [ ] Tester les relations

---

## 🚀 ORDRE D'IMPLÉMENTATION RECOMMANDÉ

### Niveau 1 : BASIQUE

1. **Category** (le plus simple, pas de dépendances)
2. **Supplier** (simple aussi)
3. **Client** (simple aussi)

### Niveau 2 : INTERMÉDIAIRE

4. **Product** (dépend de Category et Supplier)
5. **Review** (dépend de Product et User)

### Niveau 3 : AVANCÉ

6. **Order** (dépend de User et Client)
7. **OrderItem** (table intermédiaire, calculs)

---

## 💡 BONNES PRATIQUES À RESPECTER

### 1. Nommage

```python
# ✅ BON
class ProductListSerializer(serializers.ModelSerializer):
class ProductCreateSerializer(serializers.ModelSerializer):
class ProductDetailSerializer(serializers.ModelSerializer):

# ❌ MAUVAIS
class SerializersProduit(serializers.ModelSerializer):
class SerializersProduitListe(serializers.ModelSerializer):
```

### 2. Validation

```python
def validate_price(self, value):
    if value <= 0:
        raise serializers.ValidationError("Le prix doit être supérieur à 0")
    return value

def validate(self, data):
    # Validation entre plusieurs champs
    if data['stock'] == 0 and data['price'] > 1000:
        raise serializers.ValidationError("Un produit cher ne peut pas être en rupture")
    return data
```

### 3. Optimisation des requêtes

```python
queryset = Product.objects.select_related('category').prefetch_related('suppliers')
```

### 4. Permissions

```python
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
```

---

## 📊 STRUCTURE FINALE ATTENDUE

```
app/
├── models.py (déjà fait ✅)
├── serializers/
│   ├── __init__.py
│   ├── category_serializers.py
│   ├── product_serializers.py
│   ├── order_serializers.py
│   ├── review_serializers.py
│   ├── client_serializers.py
│   └── supplier_serializers.py
├── views/
│   ├── __init__.py
│   ├── category_views.py
│   ├── product_views.py
│   ├── order_views.py
│   ├── review_views.py
│   ├── client_views.py
│   └── supplier_views.py
└── urls.py
```

---

## 🎯 CRITÈRES D'ÉVALUATION

| Critère                             | Points |
| ----------------------------------- | ------ |
| Serializers complets (3 par modèle) | 30%    |
| Views CRUD fonctionnelles           | 30%    |
| URLs bien structurées               | 10%    |
| Validations personnalisées          | 10%    |
| Filtres et recherche                | 10%    |
| Code propre et commenté             | 10%    |

---

## 🔍 EXEMPLE COMPLET : CATEGORY

Voir le fichier `serializers.py` pour l'implémentation complète de Category.

---

## 📚 RESSOURCES

- Documentation DRF : https://www.django-rest-framework.org/
- Tutoriel : https://www.django-rest-framework.org/tutorial/quickstart/
- Best practices : https://learndjango.com/tutorials/

---

## ⚠️ ERREURS COURANTES À ÉVITER

1. ❌ Utiliser `models` au lieu de `model` dans Meta
2. ❌ Oublier `read_only=True` pour les champs calculés
3. ❌ Ne pas utiliser `select_related()` / `prefetch_related()`
4. ❌ Exposer des champs sensibles (mots de passe, etc.)
5. ❌ Ne pas gérer les erreurs 404
6. ❌ Oublier la pagination pour les listes
7. ❌ Ne pas valider les données en entrée

---

**Bon courage ! Commencez par Category, puis progressez vers les modèles plus complexes.**
