from django.contrib import admin
from . models import Shopper


# Admin classe
class ShopperAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

# Register your models here.
admin.site.register(Shopper, ShopperAdmin)