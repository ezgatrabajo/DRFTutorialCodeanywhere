from django.contrib.auth.models import User, Group
from .models import Categoria, Marca,Dispenser
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
