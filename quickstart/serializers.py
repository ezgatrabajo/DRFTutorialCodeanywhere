from django.contrib.auth.models import User, Group
from .models import Categoria, Marca, Dispenser, Producto, Pedido, Pedidodetalle, Parametro, Promo, Estado

from rest_framework import serializers
from rest_framework.authtoken.models import Token




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email','password')
        extra_kwargs={'password':{'write_only':True}}
        
    def create(self, validated_data):
        user = User(email = validated_data['email'], username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
      
    

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

        
class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class MarcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'nombre', 'descripcion']


class DispenserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dispenser
        fields = ['id', 'nombre', 'descripcion','serie', 'orden']



class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'


class PedidodetalleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedidodetalle
        fields = '__all__'


class PromoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Promo
        fields = '__all__'

class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'



class ParametroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'


