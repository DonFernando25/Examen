from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Usuario
from .models import Producto
from .forms import ProductoForm

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
    productos = Producto.objects.all()
    return render(request, 'Pages/EstrellaTienda.html', {'productos': productos})

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

def user_del(request, pk):
    try:
        usuario = Usuario.objects.get(rut=pk)
        usuario.delete()

        usuarios = Usuario.objects.all()
        context = {
            "mensaje": "Registro Eliminado",
            "usuarios": usuarios,
        }
        return render(request, "Crud/Lista_usuario.html", context)
    except Usuario.DoesNotExist:
        usuarios = Usuario.objects.all()
        context = {
            "mensaje": "Error, Rut no encontrado...",
            "usuarios": usuarios,
        }
        return render(request, "Crud/Lista_usuario.html", context)


def user_findEdit(request, pk):
    if pk != "":
        usuario = Usuario.objects.get(rut=pk)
        context = {
            "usuario": usuario,
        }
        return render(request, "Crud/editar_usuario.html", context)
    else:
        usuarios = Usuario.objects.all()
        context = {
            "mensaje": "Error, Rut no encontrado",
            "usuarios": usuarios,
        }
        return render(request, "Crud/Lista_usuario.html", context)

def user_update(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        nombre_usuario = request.POST["nombreUsuario"]
        correo = request.POST["correo"]
        contrasena = request.POST["contrasena"]
        fecha_nacimiento = request.POST["fechaNacimiento"]
        genero = request.POST["genero"]

        usuario = Usuario.objects.get(rut=rut)
        usuario.nombre = nombre
        usuario.apellido = apellido
        usuario.nombre_usuario = nombre_usuario
        usuario.correo = correo
        usuario.contrasena = contrasena
        usuario.fecha_nacimiento = fecha_nacimiento
        usuario.genero = genero
        usuario.save()

        context = {
            "mensaje": "Modificado con Exito",
            "usuario": usuario,
        }
        return render(request, "Crud/editar_usuario.html", context)
    else:
        return redirect("Lista_Usuarios")
    


def añadir_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('LisPro')
    else:
        form = ProductoForm()
    return render(request, 'Crud/añadir_producto.html', {'form': form})



def editar_producto(request, pk):
    producto = get_object_or_404(Producto, id_producto=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('LisPro')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'Crud/editar_producto.html', {'form': form})

def producto_eliminar(request, pk):
    producto = Producto.objects.get(id_producto=pk)
    producto.delete()
    return redirect('LisPro')

def lista_productos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'Crud/Lista_productos.html', context)