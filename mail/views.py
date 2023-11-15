
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
    usuario_logueado = request.user
    messages = Mail.objects.filter(usuario_origen=usuario_logueado).order_by("-fecha_envio")
    categorias = Categoria.objects.all().order_by("categoria")
    return render(request, 'mail/enviados.html', {'messages': messages, 'categorias': categorias})
    pass


@csrf_exempt
@login_required
def nuevo(request):
    nuevo_email = None
    if request.method == 'POST':
        email_form = MailForm(request.POST)
        if email_form.is_valid():
            nuevo_email = email_form.save(commit=False)

            nuevo_email.usuario_origen = request.user
            nuevo_email.mail_origen = request.user.email
            nuevo_email.save()

            return redirect('mail:enviados')
    else:
        email_form = MailForm(initial={'mail_origen': request.user.email})

    # Se renderiza el template 'mail/nuevo.html' y se envía en el contexto la variable "email_form"
    return render(request, 'mail/nuevo.html', {'form': email_form})



@login_required
def asignar_categoria(request):
    if request.method == 'POST':
        ids_emails_seleccionados = request.POST.getlist('mail')
        categoria_selecionada = int(request.POST.get('categoria'))
        for id_email in ids_emails_seleccionados:
            email = Mail.objects.get(id=id_email)
            if categoria_selecionada == 0:
                email.categoria = None
            else:
                email.categoria = Categoria.objects.get(id=categoria_selecionada)
            email.save()
        return redirect('mail:enviados')
    else:
        return redirect('mail:enviados')


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
