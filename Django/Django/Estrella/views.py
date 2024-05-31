from django.shortcuts import render

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

def page5(request):
    return render(request, "Pages/EstrellaFormulario.html")

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


