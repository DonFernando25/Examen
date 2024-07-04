from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from .models import Usuario,Admin,Producto
from .forms import ProductoForm,AdminForm
from .decorators import admin_required, usuario_required

# Create your views here.



def logout(request):
    auth_logout(request)
    return redirect('IniSe')

def index(request):
    return render(request, "Pages/EstrellaMacul.html")

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
    if request.method == 'POST':
        nombre_usuario = request.POST['nombre_usuario']
        contrasena = request.POST['contrasena']
        try:
            usuario = Usuario.objects.get(nombre_usuario=nombre_usuario, contrasena=contrasena)
            request.session['usuario_rut'] = usuario.rut
            return redirect('Perfil')
        except Usuario.DoesNotExist:
            return render(request, 'Pages/EstrellaIS.html', {'error': 'Credenciales inválidas'})
    return render(request, 'Pages/EstrellaIS.html')



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
    
@admin_required
def lista_usuario(request):
    usuarios = Usuario.objects.all()
    context = {
        'usuarios': usuarios,
    }
    return render(request, 'Crud/Lista_usuario.html', context)    

@admin_required
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

@admin_required
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

@admin_required
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
    

@admin_required
def añadir_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('LisPro')
    else:
        form = ProductoForm()
    return render(request, 'Crud/añadir_producto.html', {'form': form})


@admin_required
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

@admin_required
def producto_eliminar(request, pk):
    producto = Producto.objects.get(id_producto=pk)
    producto.delete()
    return redirect('LisPro')

@admin_required
def lista_productos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'Crud/Lista_productos.html', context)

@admin_required
def adduser(request):
    if request.method != "POST":
        return render(request, "Crud/añadir_usuario.html")
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
        return render(request, "Crud/Lista_usuario.html", context)

@admin_required
def añadir_admin(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        nombre_usuario = request.POST["nombreUsuario"]
        correo = request.POST["correo"]
        contrasena = request.POST["contrasena"]
        fecha_nacimiento = request.POST["fechaNacimiento"]
        genero = request.POST["genero"]
        es_admin = True  

        Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            apellido=apellido,
            nombre_usuario=nombre_usuario,
            correo=correo,
            contrasena=contrasena,
            fecha_nacimiento=fecha_nacimiento,
            genero=genero,
            es_admin=es_admin
        )
        return redirect('LisUs')  
    else:
        return render(request, 'registro_admin.html')
    

@usuario_required
def perfil(request):
    if 'usuario_rut' in request.session:
        usuario = Usuario.objects.get(rut=request.session['usuario_rut'])
        return render(request, 'Pages/EstrellaPerfil.html', {'usuario': usuario})
    return redirect('IniSe')

@admin_required
def añadir_admin(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('LisAdm')
    else:
        form = AdminForm()
    return render(request, 'Crud/añadir_admin.html', {'form': form})


def inicio_sesion_admin(request):
    if request.method == 'POST':
        nombre_usuario = request.POST['nombre_usuario']
        contrasena = request.POST['contrasena']
        try:
            admin = Admin.objects.get(nombre_usuario=nombre_usuario, contrasena=contrasena)
            request.session['admin_id'] = admin.id
            return redirect('LisPro')
        except Admin.DoesNotExist:
            return render(request, 'Crud/sesion_admin.html', {'error': 'Credenciales inválidas'})
    return render(request, 'Crud/sesion_admin.html')

def logadm(request):
    auth_logout(request)
    return redirect('IniAd')

@admin_required
def lista_admins(request):
    admins = Admin.objects.all()
    context = {
        'admins': admins,
        'mensaje': '',
    }
    return render(request, 'Crud/Lista_admin.html', context)

@admin_required
def editar_admin(request, pk):
    admin = get_object_or_404(Admin, id=pk)
    if request.method == 'POST':
        admin.nombre_usuario = request.POST['nombre_usuario']
        admin.correo = request.POST['correo']
        admin.contrasena = request.POST['contrasena']
        admin.save()
        return redirect('LisAdm')
    return render(request, 'Crud/editar_admin.html', {'admin': admin})

@admin_required
def eliminar_admin(request, pk):
    admin = get_object_or_404(Admin, id=pk)
    admin.delete()
    return redirect('LisAdm')
