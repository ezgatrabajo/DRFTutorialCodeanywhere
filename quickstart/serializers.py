from django.contrib.auth.models import User, Group
from .models import Categoria, Marca, Dispenser, Producto, Pedido, Pedidodetalle, Parametro, Promo, Estado, Unidadmedida, Track, Album

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
        fields = ['id', 'nombre', 'marcaId','descripcion','preciounitario', 'marca','categoria','categoriaId' ,'codigoexterno', 'stock', 'imagen', 'enabled', 'ispromo', 'preciopromo','unidadmedida','unidadmedidaId' ,'isfraccionado']


class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'








class PedidodetalleSerializer(serializers.HyperlinkedModelSerializer):
    producto = ProductoSerializer(many=False, read_only=True)
    productoId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Producto.objects.all(), source='producto')


    class Meta:
        model = Pedidodetalle
        fields = ['cantidad', 'producto','productoId']




class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    items     = PedidodetalleSerializer(many=True)
    estado = EstadoSerializer(many=False, read_only=True)
    estadoId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Estado.objects.all(), source='estado')
    cliente = UserSerializer(many=False, read_only=True)
    clienteId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='cliente')

    def create(self, validated_data):
        print(validated_data)

        tracks_data = validated_data.pop('items')
        print(tracks_data)

        pedido = Pedido.objects.create(**validated_data)
        for track_data in tracks_data:
            Pedidodetalle.objects.create(pedido=pedido, **track_data)
        return pedido


    class Meta:
        model = Pedido
        fields = ['android_id','estado','estadoId','cliente','clienteId',
                  'subtotal','monto',
                  'localidad','calle','nro','telefono','contacto','items'
                  ]











#tutorial
class TrackSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(many=False, read_only=True)
    productoId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Producto.objects.all(), source='producto')

    class Meta:
        model = Track
        fields = ['cantidad','producto','productoId']



class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ['android_id', 'localidad', 'tracks']

    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)

        for track_data in tracks_data:
            print(track_data)
            Track.objects.create(album=album, **track_data)
        return album





class PromoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Promo
        fields = '__all__'



class ParametroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parametro
        fields = '__all__'




