
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import HttpResponseRedirect, render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .forms import MailForm
from .models import User, Mail, Categoria


@login_required
def enviados(request):
    # Completar aqui.
    # Renderizar el template "mail/enviados.html" enviando como variables de contexto: una lista de los mails enviados
    # por el usuario logueado ordenados por fecha de envio en forma descendente; y una lista de todas las categorias
    # ordenadas por nombre

    # Fin Completar aqui
    pass


@csrf_exempt
@login_required
def nuevo(request):
    nuevo_email = None
    if request.method == 'POST':
        email_form = MailForm(request.POST)
        if email_form.is_valid():
            # Completar aqui.
            # Se deben guardar los datos que provienen del formulario pero sin aplicar los cambios
            # a la B.D. (commit=False). Luego se debe asignar a la instancia devuelta por el Form, los campos "usuario_origen"
            # y "mail_origen" de acuerdo a los datos del usuario logueado. Finalmente, guardar los datos del objeto en la B.D.


            # Fin Completar aqui
            messages.success(request,
                             'Se ha enviado correctamente el Email a {}'.format(nuevo_email.destinatario))

            # Completar aqui. Redireccionar el control a la vista "enviados"

            # Fin Completar aqui
    else:
        # Se inicializa el Formulario con el valor correspondiente del campo "mail_origen" de acuerdo a los datos del usuario
        email_form = MailForm(initial={'mail_origen': request.user.email})

    # Completar aqui. Renderizar el template 'mail/nuevo.html' y enviar en el contexto la variable "email_form"

    # Fin Completar aqui


@login_required
def asignar_categoria(request):
    # Completar aqui.
    # Si los datos se enviaron por el método POST, obtener la lista de ids de emails seleccionados, haciendo:
    #    ids_emails_seleccionados = request.POST.getlist('mail')
    # Luego, obtener el ID de la categoria seleccionada en el combo y recuperar la instancia de categira de acuerdo a ese ID.
    # Si la categoria tiene el valor '0' (Ninguna), actualizar los registros de emails seleccionados con "categoria=None".
    # Caso contrario, actualizar los registros de emails seleccionados con la categoria seleccionada.
    # Finalmente, redireccionar el control a la vista "enviados"


    # Fin Completar aqui
    pass


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("mail:enviados"))
        else:
            return render(request, "mail/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("mail:enviados"))

        return render(request, "mail/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("mail:login"))


def register(request):
    if request.method == "POST":
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "mail/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "mail/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("mail:enviados"))
    else:
        return render(request, "mail/register.html")
