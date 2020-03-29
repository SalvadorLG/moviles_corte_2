from rest_framework import serializers
from tienda.models import userProfile, Producto, Detalles
class userProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = userProfile
        fields = '__all__'

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class DetallesSerializer(serializers.ModelSerializer):
    userprofile_name = userProfileSerializer(many=True, read_only=True)

    producto_name = ProductosSerializer(many=True, read_only=True)

    class Meta:
        model = Detalles
        fields = ('__all__')