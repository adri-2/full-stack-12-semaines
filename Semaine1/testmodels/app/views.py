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


from rest_framework import generics, filters, status,viewsets
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
    #     queryset = Category.objects.all().annotate(products_count=Count('products'))
        
    #     return queryset
class CategoryDetailView(generics.RetrieveAPIView):
    serializer_class =CategoryDetailSerializer
    queryset=Category.objects.all()   
    
    # def get_queryset(self):
    #     queryset = Category.objects.all().prefetch_related('products')
    #     return queryset
    # lookup_field = 'id'  # 👈 On dit à la vue d’utiliser "id" au lieu de "pk"

    
    
class CategoryDeleteView(generics.DestroyAPIView):
    serializer_class =CategoryDetailSerializer
    queryset=Category.objects.all()   
    



# ============================================================================
# 📁 SUPPLIER VIEWSET
# ============================================================================

# TODO 1: Créer SupplierViewSet
# CONSIGNES :
# - Hériter de ModelViewSet
# - Utiliser les 3 serializers selon l'action
# - Ajouter la recherche sur 'name', 'contact_name', 'email'
# - Ajouter le tri sur 'name', 'created_at'
# - Permissions : IsAuthenticatedOrReadOnly

class SupplierViewSet(viewsets.ModelViewSet):
    """
    📦 TODO : ViewSet pour gérer les fournisseurs 
    """
    queryset = Supplier.objects.all()
    # TODO: permission_classes
    # TODO: filter_backends
    # TODO: search_fields
    # TODO: ordering_fields
    # TODO: ordering
    
    def get_serializer_class(self):
        """TODO : Retourner le bon serializer selon l'action"""
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            from .serializers import SupplierCreateSerializer
            return SupplierCreateSerializer
        elif self.action == 'list':
            from .serializers import SupplierListSerializer
            return SupplierListSerializer
        else:
            from .serializers import SupplierDetailSerializer
            return SupplierDetailSerializer
    
    def get_queryset(self):
        """TODO : Optimiser les requêtes"""
        queryset = Supplier.objects.all()
        # TODO: Ajouter des annotations si nécessaire
        # Optimisation : précharger les produits pour éviter le N+1 query problem
        if self.action == 'list':
            queryset = queryset.annotate(products_count=Count('products'))
        elif self.action == 'retrieve':
            queryset = queryset.prefetch_related('products')
        return queryset
    
    # TODO: Action personnalisée 'products' - Liste des produits d'un fournisseur
    # @action(detail=True, methods=['get'])
    # def products(self, request, pk=None):
    #     pass

    
    
    