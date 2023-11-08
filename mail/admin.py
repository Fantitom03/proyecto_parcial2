from django.contrib import admin

# Register your models here.
from mail.models import Categoria, User

admin.site.register(Categoria)
admin.site.register(User)