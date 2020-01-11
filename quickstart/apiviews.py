from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from .models import Categoria, Marca, Dispenser
from rest_framework import viewsets, generics
from .serializers import *
from .permissions import Iscliente, Isdeveloper, Isempleado, Isempresa


#TABLAS DEL SISTEMA
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
      
    
class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
  permission_classes=()
  
  def post(self, request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    
    if user:
      return Response({"token":user.auth_token.key})
    else:
      return Response ({"error":"Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
  

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


#Tablas del NEGOCIOs
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def get_permissions(self):
        if self.request.method == 'POST' or self.request.method == 'DELETE' or self.request.method == 'PUT':
            self.permission_classes = [Isdeveloper | Isempresa]
        return super(CategoriaViewSet, self).get_permissions()

    
class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

    def get_permissions(self):
        if self.request.method == 'POST' or self.request.method == 'DELETE' or self.request.method == 'PUT':
            self.permission_classes = [Isdeveloper|Isempresa]
        return super(MarcaViewSet, self).get_permissions()

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_permissions(self):
        if self.request.method == 'POST' or self.request.method == 'DELETE' or self.request.method == 'PUT':
            self.permission_classes = [Isdeveloper|Isempresa]
        return super(ProductoViewSet, self).get_permissions()




class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def get_permissions(self):
        if self.request.method == 'POST' or self.request.method == 'DELETE' or self.request.method == 'PUT':
            self.permission_classes = [Isdeveloper | Isempresa]
        return super(PedidoViewSet, self).get_permissions()


class PedidodetalleViewSet(viewsets.ModelViewSet):
    queryset = Pedidodetalle.objects.all()
    serializer_class = PedidodetalleSerializer

    def get_permissions(self):
        if self.request.method == 'POST' or self.request.method == 'DELETE' or self.request.method == 'PUT':
            self.permission_classes = [Isdeveloper | Isempresa]
        return super(PedidodetalleViewSet, self).get_permissions()


class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

    def get_permissions(self):
        if self.request.method == 'POST' or self.request.method == 'DELETE' or self.request.method == 'PUT':
            self.permission_classes = [Isdeveloper | Isempresa]
        return super(EstadoViewSet, self).get_permissions()


class ParametroViewSet(viewsets.ModelViewSet):
    queryset = Parametro.objects.all()
    serializer_class = ParametroSerializer

    def get_permissions(self):
        if self.request.method == 'POST' or self.request.method == 'DELETE' or self.request.method == 'PUT':
            self.permission_classes = [Isdeveloper | Isempresa]
        return super(ParametroViewSet, self).get_permissions()


class PromoViewSet(viewsets.ModelViewSet):
    queryset = Promo.objects.all()
    serializer_class = PromoSerializer

    def get_permissions(self):
        if self.request.method == 'POST' or self.request.method == 'DELETE' or self.request.method == 'PUT':
            self.permission_classes = [Isdeveloper | Isempresa]
        return super(PromoViewSet, self).get_permissions()
#Fin tabla de negocios



class DispenserViewSet(viewsets.ModelViewSet):
    queryset = Dispenser.objects.all()
    serializer_class = DispenserSerializer




#Ejemplo de ApiView Custom
class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': request.user,  # `django.contrib.auth.User` instance.
            'auth': request.auth,  # None
        }
        return Response(content)