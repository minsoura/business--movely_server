from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(PointPolicy)
class PointPolicyAdmin(admin.ModelAdmin):
    pass


@admin.register(PointHistory)
class PointHistoryAdmin(admin.ModelAdmin):
    pass