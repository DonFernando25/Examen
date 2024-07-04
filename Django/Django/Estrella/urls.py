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
    path("adduser", views.adduser, name="adduser"),
    path("Eliminar_Usuario/<str:pk>/", views.user_del, name="user_del"),
    path("user_findEdit/<str:pk>", views.user_findEdit, name="user_findEdit"),
    path("EdUs", views.user_update, name="EdUs"),
    path('añadir_producto', views.añadir_producto, name='añadir_producto'),
    path('editar_producto/<str:pk>/', views.editar_producto, name='editar_producto'),
    path('Eliminar_Producto/<str:pk>/', views.producto_eliminar, name='prod_del'),
    path('LisPro', views.lista_productos, name='LisPro'),
    path('ReAd', views.añadir_admin, name='ReAd'),
    path("IniAd", views.inicio_sesion_admin, name="IniAd"),
    path('Perfil', views.perfil, name='Perfil'),
    path('logout', views.logout, name='logout'),
    path('logadm', views.logadm, name='logadm'),
    path('LisAdm', views.lista_admins, name='LisAdm'),
    path('editar_admin/<int:pk>/', views.editar_admin, name='editar_admin'),
    path('eliminar_admin/<int:pk>/', views.eliminar_admin, name='eliminar_admin'),
]
