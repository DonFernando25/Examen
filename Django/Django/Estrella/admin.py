from django.contrib import admin
from .models import  Usuario,Producto,Admin


# Register your models here.

admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Admin)

