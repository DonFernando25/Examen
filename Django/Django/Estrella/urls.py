from django.urls import path
from Estrella import views




urlpatterns = [
    path('Home',views.index,name='EstrellaMacul'),
    path("Plantel", views.page2, name="Plantel"),
    path("Historia", views.page3, name="Historia"),
    path("Tienda", views.page4, name="Tienda"),
    path("Formulario", views.page5, name="Formulario"),
]
