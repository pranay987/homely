from django.contrib import admin
from .models import Property, HomeOwner, Renter

# Register your models here.
admin.site.register(Property)
admin.site.register(HomeOwner)
admin.site.register(Renter)
