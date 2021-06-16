from django import forms
from .models import CsvImport

class CsvImportForm(forms.ModelForm):
    class Meta:
        model = CsvImport
        fields = ('file_import',)