from rest_framework import serializers


from .models import Product,Order,OrderItem


class ProdutSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields=('id','name',
            
                'price',
                'stock','description')
        
    def validate_price(self, data):
        if data <=0:
            raise serializers.ValidationError('price o null')
        return data    

class OrderItemSerializer(serializers.ModelSerializer):
    product_name=serializers.CharField(source='product.name')
    product_price=serializers.DecimalField(max_digits=10,decimal_places=2, source='product.price')
    class Meta:
        model=OrderItem
        fields=('quantity','product_price','product_name','item_subtotal')   

    
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True,read_only=True)
    total_price=serializers.SerializerMethodField()
    
    def get_total_price(self,obj):
        order_items =obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)
    class Meta:
        model=Order
        fields=('order_id','user','created_at','states','items','total_price')   

class ProductInfoSerializer(serializers.Serializer):
    # get all products 
    products = ProdutSerializer(many=True)
    count =serializers.IntegerField()
    max_price=serializers.FloatField()