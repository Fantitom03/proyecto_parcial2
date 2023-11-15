from django.urls import path

from . import views

app_name = 'mail'

urlpatterns = [
    path("", views.login_view, name="login"),
    path("enviados", views.enviados, name="enviados"),
    path("asignar_categoria",views.asignar_categoria, name="asignar_categoria"),
    path("nuevo", views.nuevo, name="nuevo"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("registro", views.register, name="registro"),
]
