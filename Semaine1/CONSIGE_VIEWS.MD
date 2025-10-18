---

## ⚖️ 1. Différence fondamentale entre `ViewSet` et `generics`

| Aspect                           | `ViewSet` / `ModelViewSet`                                         | `generics` (ex: `ListAPIView`, `CreateAPIView`, etc.) |
| -------------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------- |
| **Endpoints automatiques**       | Oui (list, create, retrieve, update, destroy)                      | Non, 1 classe = 1 endpoint                            |
| **Décorateur `@action`**         | ✅ Oui, supporté directement                                        | 🚫 Non, pas disponible nativement                     |
| **Logique métier personnalisée** | ✅ Possible via `@action`, `perform_create`, `perform_update`, etc. | ✅ Possible, mais autrement (voir plus bas)            |
| **Idéal pour**                   | APIs REST complètes et regroupées                                  | Contrôle fin, séparation du code                      |

---

## ⚙️ 2. Donc, avec les `generics`, **pas de `@action`**, mais… tu peux faire **mieux** 💪

Tu peux intégrer ta logique métier à plusieurs niveaux.

---

### 🧩 A. Dans les méthodes `perform_*`

Les `GenericAPIView` te permettent d’injecter ta logique **au moment de l’action** :

- `perform_create()`
- `perform_update()`
- `perform_destroy()`

**Exemple :**

```python
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
import logging

logger = logging.getLogger(__name__)

class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        # Exemple de logique métier
        name = serializer.validated_data.get('name')
        if "@" in name:
            raise ValueError("Le nom ne peut pas contenir de @")

        # Création de l’objet
        instance = serializer.save()

        # Exemple de log
        logger.info(f"Catégorie créée : {instance.name}")
```

✅ Avantages :

- Tu gardes la structure DRF propre
- Tu ajoutes ta logique sans casser les mixins
- Idéal pour validations, logs, envois d’e-mails, etc.

---

### 🧩 B. En surchargeant `get_queryset()` ou `get_serializer_class()`

Tu peux aussi adapter dynamiquement ce que ta vue renvoie selon le contexte :

```python
class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        user = self.request.user
        # Filtrer selon l’utilisateur
        return Category.objects.filter(owner=user)
```

---

### 🧩 C. En ajoutant des **views personnalisées** (équivalent des `@action`)

Tu peux créer une nouvelle vue **basée sur `APIView`** ou `GenericAPIView` pour un endpoint spécial.

**Exemple : endpoint `/api/categories/<id>/products/`**

```python
from rest_framework.response import Response
from rest_framework import status

class CategoryProductsView(generics.GenericAPIView):
    """
    Endpoint personnalisé équivalent à un @action(detail=True)
    """
    serializer_class = CategorySerializer  # ou un autre
    queryset = Category.objects.all()

    def get(self, request, pk):
        category = self.get_object()
        products = category.product_set.all()
        data = [p.name for p in products]
        return Response({"category": category.name, "products": data}, status=status.HTTP_200_OK)
```

Et dans ton `urls.py` :

```python
path('categories/<int:pk>/products/', CategoryProductsView.as_view(), name='category-products')
```

👉 C’est l’équivalent d’un `@action(detail=True, methods=['get'])` dans un `ViewSet`,
mais **plus explicite et mieux découplé**.

---

### 🧩 D. En combinant `APIView` pour plus de liberté

Tu peux hériter directement de `APIView` si tu veux gérer **plusieurs méthodes HTTP dans la même vue** :

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class CategoryStatsView(APIView):
    """
    Exemple d'action spéciale : statistiques
    """
    def get(self, request):
        count = Category.objects.count()
        return Response({"total_categories": count})
```

---

## ✅ En résumé

| Objectif                             | Solution avec `generics`                            |
| ------------------------------------ | --------------------------------------------------- |
| Validation avant sauvegarde          | `perform_create()` / `perform_update()`             |
| Filtrage dynamique                   | `get_queryset()`                                    |
| Changer le serializer selon l’action | `get_serializer_class()`                            |
| Ajouter un endpoint personnalisé     | Créer une nouvelle vue `GenericAPIView` / `APIView` |
| Logique métier complexe              | Inside `perform_*` ou dans un service dédié         |

---

## ⚠️ À éviter

🚫 Essayer d’utiliser `@action` sur une classe `generics` (ne fonctionnera pas).
🚫 Mettre trop de logique dans le serializer (garde la logique métier dans la vue ou un service).
🚫 Dupliquer du code entre les vues (pense à créer une `BaseView` commune).
