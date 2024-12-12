from django.shortcuts import render
from .forms import CreateImport
from .models import ImportRequest
import datetime
from django.contrib.auth.models import User
from siteutils.models import menu_items
import mimetypes
from django.http import HttpResponse

def importpage(request):
    items = menu_items.objects.all() #menu items
    today = datetime.datetime.now()
    PageTitle = 'Import Tool'
    initial_data = {'owner': request.user.id}
    form = CreateImport(request.POST,request.FILES, initial=initial_data) #Get the form to render on the pager
    context = {"form": form, "items": items, 'initial': initial_data, "PageTitle": PageTitle}
    if request.method == 'POST' and form.is_valid():
        #actually create the record
        newImport = form.save(commit=False) #instance the new import record
        newImport.owner = request.user #pins the logged in user to the new record
        newImport.save() #commit the record to the DB. 
    return render(request, 'cardImport/Import.html', context)

def download_card_template(reqeust):
    filepath = 'cardImport/CardImport_Template.csv' #full path needed with file name as well. Will get permission error if this is not full path. 
    filename = 'CardImport_Template.csv'
    file = open(filepath, 'r') 
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(file, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
