from rest_framework import serializers
from inventario.models import Productos

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ["sku","name","price","brand"]


    def create(self,validated_data):
        return Productos.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data.get("name",instance.name)
        instance.price = validated_data.get("price",instance.price)
        instance.brand = validated_data.get("brand",instance.brand)
        instance.save()
        return instance
