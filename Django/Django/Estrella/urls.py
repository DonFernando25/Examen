from django.urls import path
from Estrella import views




urlpatterns = [
    path('Home',views.index,name='EstrellaMacul'),
    path("Plantel", views.page2, name="Plantel"),
    path("Historia", views.page3, name="Historia"),
    path("Tienda", views.page4, name="Tienda"),
    path("Formulario", views.page5, name="Formulario"),
    path("Camloc", views.page6, name="Camloc"),
    path("CamVis", views.page7, name="CamVis"),
    path("CamGor", views.page8, name="CamGor"),
    path("CamBuf", views.page9, name="CamBuf"),
    path("CamGol", views.page10, name="CamGol"),
    path("IniSe", views.page11, name="IniSe"),
    path('LisUs', views.lista_usuario, name='LisUs'),
    
]
