from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Data)
admin.site.register(UserData)


