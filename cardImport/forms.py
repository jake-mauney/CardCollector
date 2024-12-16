from django import forms
from django.forms import ModelForm
from .models import ImportRequest

#Baseline model form
class CreateImport(ModelForm):
    class Meta:
        model = ImportRequest
        fields = ['csv_file', 'type'] #only adding the fields needed

class CreatImportNoType(ModelForm):
    class Meta:
        model = ImportRequest
        fields = ['csv_file']