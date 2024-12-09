from django import forms
from django.forms import ModelForm
from .models import ImportRequest

class CreateImport(ModelForm):
    class Meta:
        model = ImportRequest
        fields = ['csv_file', 'type']