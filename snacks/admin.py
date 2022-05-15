from django.contrib import admin

from .models import Snack ,HealthySnack



@admin.register(Snack)

class AdminSnack(admin.ModelAdmin):
    pass


@admin.register(HealthySnack)
class AdminHealthySnack(admin.ModelAdmin):
    list_display =['name','price','is_healthy']

