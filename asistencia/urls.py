from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from .views import (
    # Dashboard
    dashboard,

    # Integrantes
    IntegranteListView, IntegranteCreateView,
    IntegranteUpdateView, IntegranteDeleteView,

    # Reuniones
    ReunionListView, ReunionDetailView,
    ReunionCreateView, ReunionUpdateView, ReunionDeleteView,

    # Asistencia
    marcar_asistencia,
    ver_asistencia
)

urlpatterns = [

    # ---------- DASHBOARD ----------
    path('', dashboard, name='dashboard'),

    # ---------- AUTENTICACIÓN ----------
    path('login/', auth_views.LoginView.as_view(
        template_name='asistencia/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # ---------- CRUD INTEGRANTES ----------
    path('integrantes/', IntegranteListView.as_view(), name='integrante_list'),
    path('integrantes/nuevo/', IntegranteCreateView.as_view(), name='integrante_create'),
    path('integrantes/<int:pk>/editar/', IntegranteUpdateView.as_view(), name='integrante_update'),
    path('integrantes/<int:pk>/eliminar/', IntegranteDeleteView.as_view(), name='integrante_delete'),

    # ---------- CRUD REUNIONES ----------
    path('reuniones/', ReunionListView.as_view(), name='reunion_list'),
    path('reuniones/nuevo/', ReunionCreateView.as_view(), name='reunion_create'),
    path('reuniones/<int:pk>/', ReunionDetailView.as_view(), name='reunion_detail'),
    path('reuniones/<int:pk>/editar/', ReunionUpdateView.as_view(), name='reunion_update'),
    path('reuniones/<int:pk>/eliminar/', ReunionDeleteView.as_view(), name='reunion_delete'),

    # ---------- ASISTENCIA ----------
    path(
        'reuniones/<int:reunion_id>/asistencia/',
        marcar_asistencia,
        name='marcar_asistencia'
    ),
    path(
        'reuniones/<int:reunion_id>/asistencia/ver/',
        ver_asistencia,
        name='ver_asistencia'
    ),

    path(
    'integrantes/exportar/',
    views.IntegranteExportExcelView.as_view(),
    name='integrante_export_excel'
    ),

    path(
    'reunion/<int:reunion_id>/exportar-excel/',
    views.exportar_asistencia_excel,
    name='exportar_asistencia_excel'
    ),
    
    path('integrante/<int:pk>/', views.integrante_perfil, name='integrante_perfil'),

    path(
        'integrante/<int:pk>/cambiar-foto/',
        views.integrante_cambiar_foto,
        name='integrante_cambiar_foto'
    ),

    path(
    'integrante/<int:pk>/editar-descripcion/',
    views.integrante_editar_descripcion,
    name='integrante_editar_descripcion'
    ),

    path(
    'integrante/<int:pk>/toggle-activo/',
    views.integrante_toggle_activo,
    name='integrante_toggle_activo'
    ),

]

