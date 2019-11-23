from django.contrib import admin
from .models import Categoria, Marca, Dispenser


class CategoriaAdmin(admin.ModelAdmin):
    fields = ['name', 'description']

class MarcaAdmin(admin.ModelAdmin):
    fields = ['name', 'description']


class DispenserAdmin(admin.ModelAdmin):
    fields = ['nombre', 'descripcion','serie', 'orden']

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Dispenser, DispenserAdmin)