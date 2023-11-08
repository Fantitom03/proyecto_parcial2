from django.urls import path

from . import views

app_name = 'mail'

urlpatterns = [
    path("", views.login_view, name="login"),
    # Completar aqui. Agregar los patrones de url para acceder a las vistas de "enviados", "nuevo" y "asignar_categoria"

    # Fin Completar aqui
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("registro", views.register, name="registro"),
]
