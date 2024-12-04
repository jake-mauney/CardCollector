from django.shortcuts import render

def importpage(request):
    return render(request, 'cardImport/Import.html')
