from django.shortcuts import render
from .forms import CreateImport
from .models import ImportRequest
import datetime
from siteutils.models import menu_items

def importpage(request):
    items = menu_items.objects.all()
    form = CreateImport(request.POST or None)
    context = {"form": form, "items": items}
    if request.method == 'POST' and form.is_valid():
        #actually create the record
        newImport = ImportRequest.objects.create(request_date = datetime.datetime.now(), csv_file = form.data('csv_file'), type = form.cleaned_data('type')) 
    return render(request, 'cardImport/Import.html', context)
