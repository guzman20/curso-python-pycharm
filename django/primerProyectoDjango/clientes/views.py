from django.shortcuts import render

from clientes.models import Cliente


# Create your views here.
def aniadir_cliente(request):
    nombre = None
    apellidos = None
    dni = None
    email = None
    pagina_destino = "aniadir_cliente.html"
    if request.method == "POST":
        pagina_destino = "bienvenido.html"
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        dni = request.POST['dni']
        email = request.POST['email']
        if nombre is not None and apellidos is not None and dni is not None and email is not None:
            cliente = Cliente(nombre, apellidos, dni, email)
        return render(request, pagina_destino)
    return render(request, pagina_destino)
