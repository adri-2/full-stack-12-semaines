from rest_framework import serializers
from .models import Product,Category



class CategorySerializers(serializers.ModelSerializer):
   
    class Meta:
        model = Category
        fields = ['name']

class CategorySerializersList(serializers.ModelSerializer):
    product_names = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['name', 'product_names']
   
    def get_product_names(self, obj):
        return [product.name for product in obj.products.all()]
    
    
   

class SerializersProduit(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category']
        
    def validate_price(self, value):
        if value <=0:
            raise serializers.ValidationError('le prix doit etre > et != de 0')
        return  value
    
    def validate_description(self, value):
        if self.initial_data.get('name') not in value:
            raise serializers.ValidationError('La description doit contenir le nom du produit.')
        return value

        
class ProduitSerializersListe(serializers.ModelSerializer):
    category_name=serializers.CharField(source='category.name')
    class Meta:
        model = Product
        fields = ['name', 'price', 'description','category_name']        