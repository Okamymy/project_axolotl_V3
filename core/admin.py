from django.contrib import admin

# Register your models here.
from .models import Recamara, Bano, Cocina, Comedor, Sala, Oficina

@admin.register(Recamara)
class RecamaraAdmin(admin.ModelAdmin):
    list_display = [
        "recamara_name",
        "imagen",
        "descripcion",
        "stock",
        "precio",
        "status",
        "codigo",
    ]

@admin.register(Bano)
class BanoAdmin(admin.ModelAdmin):
    list_display = [
        "bano_name",
        "imagen",
        "descripcion",
        "stock",
        "precio",
        "status",
        "codigo",
    ]

@admin.register(Cocina)
class CocinaAdmin(admin.ModelAdmin):
    list_display = [
        "cocina_name",
        "imagen",
        "descripcion",
        "stock",
        "precio",
        "status",
        "codigo",
    ]

@admin.register(Comedor)
class ComedorAdmin(admin.ModelAdmin):
    list_display = [
        "comedor_name",
        "imagen",
        "descripcion",
        "stock",
        "precio",
        "status",
        "codigo",
    ]

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = [
        "sala_name",
        "imagen",
        "descripcion",
        "stock",
        "precio",
        "status",
        "codigo",
    ]

@admin.register(Oficina)
class OficinaAdmin(admin.ModelAdmin):
    list_display = [
        "oficina_name",
        "imagen",
        "descripcion",
        "stock",
        "precio",
        "status",
        "codigo",
    ]