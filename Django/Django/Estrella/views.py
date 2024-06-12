from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario

# Create your views here.

def index(request):
    context={
        "usuario": "Fer",
    }
    return render(request, "Pages/EstrellaMacul.html",context)

def page2(request):
    return render(request, "Pages/EstrellaPlantel.html")

def page3(request):
    return render(request, "Pages/EstrellaHistoria.html")

def page4(request):
    return render(request, "Pages/EstrellaTienda.html")



def page6(request):
    return render(request, "Pages/EstrellaCl.html")

def page7(request):
    return render(request, "Pages/EstrellaCv.html")

def page8(request):
    return render(request, "Pages/EstrellaG.html")

def page9(request):
    return render(request, "Pages/EstrellaB.html")

def page10(request):
    return render(request, "Pages/EstrellaGoleador.html")

def page11(request):
    return render(request, "Pages/EstrellaIS.html")

def page5(request):
    if request.method != "POST":
        return render(request, "pages/EstrellaFormulario.html")
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        nombre_usuario = request.POST["nombreUsuario"]
        correo = request.POST["correo"]
        contrasena = request.POST["contrasena"]
        fecha_nacimiento = request.POST["fechaNacimiento"]
        genero = request.POST["genero"]

        obj = Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            apellido=apellido,
            nombre_usuario=nombre_usuario,
            correo=correo,
            contrasena=contrasena,
            fecha_nacimiento=fecha_nacimiento,
            genero=genero,
        )
        obj.save()
        context = {
            "mensaje": "Registro Exitoso",
        }
        return render(request, "pages/EstrellaFormulario.html", context)
    


def lista_usuario(request):
    usuarios = Usuario.objects.all()
    context = {
        'usuarios': usuarios,
    }
    return render(request, 'Crud/Lista_usuario.html', context)    



