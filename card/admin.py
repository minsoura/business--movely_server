from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('username', 'partner_name', 'created_at',)

    def username(self, obj):
        return obj.user.username

    def partner_name(self, obj):
        return obj.partner.username
