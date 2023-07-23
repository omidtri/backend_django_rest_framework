from rest_framework import serializers
from products import models
from order.models import Order

class SerializerCategoryModel(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'






class SerializerBrandModel(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = '__all__'





class SerializerSizeModel(serializers.ModelSerializer):
    class Meta:
        model = models.Size
        fields = '__all__'


class SerializerMetrajModel(serializers.ModelSerializer):
    class Meta:
        model = models.Metraj
        fields = '__all__'


# get all product just product dont detail
class SerializerModel(serializers.ModelSerializer):
    category = SerializerCategoryModel(read_only=True, many=True)
    brand = SerializerBrandModel()
    class Meta:
        model = models.Product
        fields = '__all__'


# get detail product
class SerializerDetailModel(serializers.ModelSerializer):
    product = SerializerModel()
    metraj = SerializerMetrajModel()
    size = SerializerSizeModel() 
    class Meta:
        model = models.ProductAttribute
        fields = '__all__'
    def get_product(self, obj):
        breakpoint()
        return obj.product
    



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'