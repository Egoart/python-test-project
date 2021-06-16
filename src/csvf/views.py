from django.shortcuts import render
from .forms import CsvImportForm
from .models import CsvImport
import csv

# Create your views here.

def csv_import_view(request):
    form = CsvImportForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvImportForm()
        obj = CsvImport.objects.get(pk=10)
        with open(obj.file_import.path, 'r') as f:
            reader = csv.reader(f)

            for i, row in enumerate(reader):
                if i==0:
                    pass
                else:
                    #print(row)
                    pass

    return render(request, 'csvf/import_csv.html', {'form':form})