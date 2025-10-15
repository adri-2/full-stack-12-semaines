"""
🎯 VIEWS - EXERCICES PRATIQUES

CONSIGNES :
-----------
Pour chaque modèle, créer un ViewSet complet avec toutes les opérations CRUD :
- List (GET /api/model/)
- Create (POST /api/model/)
- Retrieve (GET /api/model/{id}/)
- Update (PUT/PATCH /api/model/{id}/)
- Destroy (DELETE /api/model/{id}/)

RÈGLES OBLIGATOIRES :
--------------------
✅ Utiliser ModelViewSet pour le CRUD complet
✅ Utiliser le bon serializer selon l'action (get_serializer_class)
✅ Ajouter des filtres (filter_backends)
✅ Ajouter la pagination
✅ Ajouter des actions personnalisées quand nécessaire
✅ Gérer les permissions

MÉTHODES À CONNAÎTRE :
---------------------
- get_serializer_class() : Choisir le serializer selon l'action
- get_queryset() : Optimiser les requêtes avec select_related/prefetch_related
- perform_create() : Logique supplémentaire à la création
- @action : Créer des endpoints personnalisés
"""


from rest_framework import generics, filters, status
from rest_framework.response import Response
from .models import Category, Product, Order, OrderItem, Review, Client, Supplier
from .serializers import CategorySerializer,CategoryListSerializer,CategoryDetailSerializer
from django.db.models import Count


# Create your views here.
# ============================================================================
# 📁 CATEGORY VIEWSET (EXEMPLE COMPLET - ÉTUDIEZ-LE)
# ============================================================================

class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    queryset=Category.objects.all()

class CategoryListView(generics.ListAPIView):
    serializer_class =CategoryListSerializer
    queryset=Category.objects.all()   
    
    # def get_queryset(self):
        
    #     return (Category.objects.annotate(product_count=Count('products')).filter(product_count__gt=0))
    
class CategoryDetailView(generics.RetrieveAPIView):
    serializer_class =CategoryDetailSerializer
    queryset=Category.objects.all()   
    # lookup_field = 'id'  # 👈 On dit à la vue d’utiliser "id" au lieu de "pk"

    
    
class CategoryDeleteView(generics.DestroyAPIView):
    serializer_class =CategoryDetailSerializer
    queryset=Category.objects.all()   
    
    