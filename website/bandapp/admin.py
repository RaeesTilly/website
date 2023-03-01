# created and registered the bandapp to an admin site which is our database site
from django.contrib import admin
from . models import band

# Register your models here.
admin.site.register(band)
