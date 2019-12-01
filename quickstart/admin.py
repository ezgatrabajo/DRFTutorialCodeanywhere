from django.contrib import admin
from .models import Categoria, Marca, Producto, Dispenser, Pedido, Unidadmedida, Pedidodetalle, Parametro, Estado


class CategoriaAdmin(admin.ModelAdmin):
    fields = ['name', 'description']

class MarcaAdmin(admin.ModelAdmin):
    fields = ['name', 'description']

class UnidadmedidaAdmin(admin.ModelAdmin):
    fields = ['nombre', 'descripcion']

class ProductoAdmin(admin.ModelAdmin):
    field = (('nombre', 'descripcion'),'preciounitario')

class PedidodetalleInline(admin.TabularInline):
    model = Pedidodetalle
    fields = ['cantidad','pedido', 'producto']


class PedidoAdmin(admin.ModelAdmin):
    #field = (('fecha', 'monto'),'cliente')
    readonly_fields = ['fecha']
    fieldsets = (
        (None, {
            'fields': ( 'cliente', 'enviodomicilio')
        }),
        ('Totales', {
            'classes': ('collapse',),
            'fields': ('subtotal', 'monto', 'montodescuento', 'cantidaddescuento', 'montoabona'),
        }),
        ('Tiempos del Pedido', {
            'classes': ('collapse',),
            'fields': ( 'impreso', 'tiempodemora', 'horarecepcion', 'horaentrega'),
        }),
        ('Datos de Entrega', {
            'classes': ('collapse',),
            'fields': ('contacto','localidad', 'calle','nro','piso', 'telefono'),
        }),
    )
    inlines = [
        PedidodetalleInline,
    ]


class EstadoAdmin(admin.ModelAdmin):
    #model = Estado
    fields = ['nombre', 'descripcion']

class ParametroAdmin(admin.ModelAdmin):
    fields = ['nombre', 'descripcion','valortexto','valorinteger' ,'valordecimal', 'valorfecha' ]

class DispenserAdmin(admin.ModelAdmin):
    fields = ['nombre', 'descripcion','serie', 'orden']

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Pedido, PedidoAdmin)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Unidadmedida, UnidadmedidaAdmin)

admin.site.register(Estado, EstadoAdmin)
admin.site.register(Parametro, ParametroAdmin)
admin.site.register(Dispenser, DispenserAdmin)
