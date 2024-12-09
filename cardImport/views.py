from django.shortcuts import render
from .forms import CreateImport
from .models import ImportRequest
import datetime
from siteutils.models import menu_items

def importpage(request):
    items = menu_items.objects.all() #menu items
    today = datetime.datetime.now()
    form = CreateImport(request.POST,request.FILES, initial={'request_date': today}) #Get the form to render on the page
    context = {"form": form, "items": items}
    if request.method == 'POST' and form.is_valid():
        #actually create the record
        form.save()
    return render(request, 'cardImport/Import.html', context)
