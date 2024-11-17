from django.template import Context

def menu_context(request):
    nav_menu = "NAV" 
    c = Context({'nav_menu': nav_menu})
    return c