from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Integrante, Reunion, Asistencia


@admin.register(Integrante)
class IntegranteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "tipo", "telefono")
    search_fields = ("nombre", "apellido")

@admin.register(Reunion)
class ReunionAdmin(admin.ModelAdmin):
    list_display = ("tema", "fecha", "maestro","tipo")
    list_filter = ("fecha",)

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('integrante', 'reunion', 'estado', 'comentario')

    def estado(self, obj):
        return "Asistió" if obj.presente else "No asistió"
    estado.short_description = "Asistencia"

    list_filter = ('presente', 'reunion')
