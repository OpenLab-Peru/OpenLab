# Python imports


# Django imports
from django.contrib import admin

# Third party apps imports


# Local imports
from .models import Document, Person

# Register your models here.
admin.site.register(Document)
admin.site.register(Person)
