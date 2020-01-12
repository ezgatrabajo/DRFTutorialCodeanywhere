from django.contrib.auth.models import User, Group
from .models import Categoria, Marca, Dispenser, Producto, Pedido, Pedidodetalle, Parametro, Promo, Estado, Unidadmedida

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



class UnidadmedidaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unidadmedida
        fields = '__all__'


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    marca        = MarcaSerializer(read_only=True)
    marcaId      = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Marca.objects.all(), source='marca')
    categoria    = CategoriaSerializer(read_only=True)
    categoriaId  = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Categoria.objects.all(), source='categoria')
    unidadmedida = UnidadmedidaSerializer(read_only=True)
    unidadmedidaId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Unidadmedida.objects.all(), source='unidadmedida')

    class Meta:
        model = Producto
        fields = ['nombre', 'marcaId','descripcion','preciounitario', 'marca','categoria','categoriaId' ,'codigoexterno', 'stock', 'imagen', 'enabled', 'ispromo', 'preciopromo','unidadmedida','unidadmedidaId' ,'isfraccionado']


class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'


class PedidodetalleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedidodetalle
        fields = '__all__'

class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    cliente = UserSerializer()
    estado  = EstadoSerializer()
    items   = PedidodetalleSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['fecha','cliente','estado','items']
        read_only_fields = ['cliente','estado']

    def create(self, validated_data):
        cliente_data = validated_data.pop('cliente')
        pedido = Pedido.objects.create(**validated_data)
        Pedido.objects.create(pedido=pedido, **cliente_data)
        return pedido


class PromoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Promo
        fields = '__all__'



class ParametroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parametro
        fields = '__all__'




