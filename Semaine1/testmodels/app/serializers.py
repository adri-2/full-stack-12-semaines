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
from .models import Product,Category,Supplier,OrderItem,Order,Client


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
  

# ============================================================================
# 📁 CLIENT SERIALIZERS
# ============================================================================

# TODO 4: Créer les 3 serializers pour Client
# CONSIGNES :
# - ClientCreateSerializer : first_name, last_name, email, phone_number, address
# - ClientListSerializer : id, first_name, last_name, email, orders_count
# - ClientDetailSerializer : tous les champs + liste des commandes

class ClientCreateSerializer(serializers.ModelSerializer):
    """
    ✍️ TODO : À compléter
    """
    class Meta:
        model = Client
        fields = [ 'first_name', 'last_name', 'email', 'phone_number', 'address']  # TODO
    
    # TODO: Validation sur email (vérifier qu'il est unique)
    # TODO: Validation sur first_name et last_name (min 2 caractères)
    def validate_first_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Le prénom doit contenir au moins 2 caractères.")
        return value

    def validate_last_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Le nom doit contenir au moins 2 caractères.")
        return value

    
    


class ClientListSerializer(serializers.ModelSerializer):
    """
    📋 TODO : À compléter
    """
    # TODO: Ajouter orders_count
    orders_count =serializers.SerializerMethodField()
    # TODO: Ajouter full_name (combinaison de first_name et last_name)
    full_name =serializers.SerializerMethodField()
    
    class Meta:
        model = Client
        fields = [ 'first_name', 'last_name', 'email', 'phone_number', 'address','orders_count','full_name']   # TODO
        
    def get_orders_count(self, obj):
        
        return obj.orders.count()
    
    def get_full_name(self, obj):
        first_name=obj.first_name or""
        last_name=obj.last_name or ""
        full_name=f"{first_name} {last_name}".strip()
        
        return full_name


class ClientDetailSerializer(serializers.ModelSerializer):
    """
    🔍 TODO : À compléter
    """
    # TODO: Ajouter la liste des commandes
    orders_list =serializers.SerializerMethodField()
    # TODO: Ajouter le montant total dépensé
    total_price =serializers.SerializerMethodField()
    
    class Meta:
        model = Client
        fields = '__all__'
        
        
    def get_orders_list(self, obj):
        return [[order.user,order.client,order.status] for order in obj.orders.all()[:5]]
    
        
    def get_total_price(self, obj):    
        
        return obj.orders_subtotal
    