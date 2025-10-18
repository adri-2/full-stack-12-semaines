"""
🎯 SERIALIZERS - EXERCICES PRATIQUES

CONSIGNES :
-----------
Pour chaque modèle, créer 3 serializers :
1. CreateSerializer - Pour créer des objets (accepte les IDs)
2. ListSerializer - Pour lister (léger, sans relations imbriquées)
3. DetailSerializer - Pour afficher les détails complets (avec relations)

RÈGLES OBLIGATOIRES :
--------------------
✅ Utiliser ModelSerializer
✅ Toujours définir 'model' et 'fields' dans Meta
✅ Ajouter des validations personnalisées
✅ Utiliser SerializerMethodField pour les champs calculés
✅ Mettre read_only=True sur les champs calculés

ORDRE D'IMPLÉMENTATION :
-----------------------
1. Category (FAIT comme exemple ✅)
2. Supplier (TODO - À FAIRE)
3. Client (TODO - À FAIRE)
4. Product (TODO - À FAIRE)
5. Review (TODO - À FAIRE)
6. Order (TODO - À FAIRE)
7. OrderItem (TODO - À FAIRE)
"""

from rest_framework import serializers
from .models import Product,Category,Supplier,OrderItem,Order


# ============================================================================
# 📁 CATEGORY SERIALIZERS (EXEMPLE COMPLET - ÉTUDIEZ-LE)
# ============================================================================

class CategorySerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Category
        fields = ['name','description']
        
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Le nom doit contenir au moins 3 caractères.")
                    
        return value.strip().title() 
   

class CategoryListSerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id','name', 'description','products_count','created_at']
    
    def get_products_count(self, obj):
        return obj.products.count()
   
   
    
class CategoryDetailSerializer(serializers.ModelSerializer):
    product_names = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id','name','description', 'product_names','created_at']   
        
    def get_product_names(self, obj):
        return [ product.name  for product in obj.products.all()[:5]]
    
    

# ============================================================================
# 📁 SUPPLIER SERIALIZERS
# ============================================================================

# TODO 1: Créer SupplierCreateSerializer
# CONSIGNES :
# - Champs : name, contact_name, email, phone_number, address
# - Validation : email doit être valide (déjà géré par EmailField)
# - Validation : name doit faire au moins 2 caractères

class SupplierCreateSerializer(serializers.ModelSerializer):
    """
    ✍️ TODO : Compléter ce serializer pour créer un fournisseur
    """
    class Meta:
        model = Supplier
        # TODO: Définir les fields
        fields = ['name', 'contact_name', 'email', 'phone_number', 'address']  # ⚠️ REMPLACER par la liste explicite des champs
    
    # TODO: Ajouter une validation sur 'name'
    def validate_name(self, data):
        if len(data) < 3:
            raise serializers.ValidationError('name doit faire au moins 2 caractères')
        return data


# TODO 2: Créer SupplierListSerializer
# CONSIGNES :
# - Champs : id, name, email, products_count
# - products_count : utiliser SerializerMethodField pour compter les produits

class SupplierListSerializer(serializers.ModelSerializer):
    """
    📋 TODO : Serializer pour lister les fournisseurs
    """
    # TODO: Ajouter products_count avec SerializerMethodField
    products_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'email', 'products_count']  # TODO: Compléter
    
    # TODO: Implémenter get_products_count
    def get_products_count(self, obj):
        return obj.products.count()


# TODO 3: Créer SupplierDetailSerializer
# CONSIGNES :
# - Tous les champs du modèle
# - Ajouter la liste des produits fournis (nom et prix seulement)

class SupplierDetailSerializer(serializers.ModelSerializer):
    """
    🔍 TODO : Serializer pour les détails complets d'un fournisseur
    """
    # TODO: Ajouter un champ 'products' avec SerializerMethodField
    products = serializers.SerializerMethodField()
    products_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Supplier
        fields =  ['id', 'name', 'email','contact_name','address', 'products_count','products']  # TODO: Être plus explicite
    
    # TODO: Implémenter get_products
    
    def get_products(self, obj):
        return [product.name for product in obj.products.all()[:5] ]
    
    def get_products_count(self, obj):
        return obj.products.count()
  