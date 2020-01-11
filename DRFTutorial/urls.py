"""DRFTutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from quickstart import apiviews, views

router = routers.DefaultRouter()
router.register(r'users', apiviews.UserViewSet)
router.register(r'groups', apiviews.GroupViewSet)
router.register(r'categorias', apiviews.CategoriaViewSet)
router.register(r'marcas', apiviews.MarcaViewSet)
router.register(r'productos', apiviews.ProductoViewSet)

router.register(r'pedidos', apiviews.PedidoViewSet)
router.register(r'pedidodetalles', apiviews.PedidodetalleViewSet)
router.register(r'promos', apiviews.PromoViewSet)
router.register(r'estados', apiviews.EstadoViewSet)
router.register(r'parametros', apiviews.ParametroViewSet)

router.register(r'dispensers', apiviews.DispenserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index, name='index'),
    path('v1/', include(router.urls)),
    path('v1/example/',apiviews.ExampleView.as_view()),
    path('v1/user/create/',apiviews.UserCreate.as_view(), name="user_create"),
    path('v1/user/login/',apiviews.LoginView.as_view(), name="user_login"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('admin/', admin.site.urls),  
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('home/', views.home)
    
    
    #path('authsocial/', include('rest_framework_social_oauth2.urls')),
]