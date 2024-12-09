from django.contrib import admin
from .models import ImportRequest

#added the import reqeust to the admin site
admin.site.register(ImportRequest)
