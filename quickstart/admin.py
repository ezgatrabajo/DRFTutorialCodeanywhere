from django.contrib import admin
from .models import Categoria, Marca


class CategoriaAdmin(admin.ModelAdmin):
    fields = ['name', 'description']

class MarcaAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Marca, MarcaAdmin)