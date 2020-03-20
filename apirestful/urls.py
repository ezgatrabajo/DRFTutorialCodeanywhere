from django.urls import include, path
from rest_framework import routers
from . import apiviews
from . import views
from rest_framework.authtoken import views as views_token


router = routers.DefaultRouter()
router.register(r'users', apiviews.UserViewSet)
router.register(r'groups', apiviews.GroupViewSet)
router.register(r'categorias', apiviews.CategoriaViewSet)
router.register(r'marcas', apiviews.MarcaViewSet)
router.register(r'productos', apiviews.ProductoViewSet)
router.register(r'unidadmedida', apiviews.UnidadmedidaViewSet)
router.register(r'pedidos', apiviews.PedidoViewSet)
router.register(r'pedidodetalles', apiviews.PedidodetalleViewSet)
router.register(r'promos', apiviews.PromoViewSet)
router.register(r'estados', apiviews.EstadoViewSet)
router.register(r'parametros', apiviews.ParametroViewSet)
router.register(r'dispensers', apiviews.DispenserViewSet)
router.register(r'tracks', apiviews.TrackViewSet)
router.register(r'albums', apiviews.AlbumViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('user/create/', apiviews.UserCreate.as_view(), name="user_create"),
    path('user/login/', apiviews.LoginView.as_view(), name="user_login"),
    path('api-token-auth/', views_token.obtain_auth_token)

]