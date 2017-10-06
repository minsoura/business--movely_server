from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Media)
class UserMediaAdmin(admin.ModelAdmin):
    pass
