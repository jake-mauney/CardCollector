from django.shortcuts import render, redirect
from django.http import HttpResponse
from cards.models import Card
from decks.models import Deck, DeckEntry
from django.db.models import Count
from siteutils.models import menu_items
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from tournament.views import TourHome
from django.contrib.auth import logout

 #grab the menu items to be used within this file

def index(request): #home/login page
    if request.user.is_authenticated: #if user is logged in goes to index.html template
        logUser = request.user
        items = menu_items.objects.filter(login_logout = 'LOGIN')
        context = {"items": items, "user": logUser }
        return render(request, 'mysite/index.html', context)
    else:
        if request.method == "POST": #if user is not logged in check to see if login post 
            username = request.POST.get('username') 
            pwd = request.POST.get('password')  
            user = authenticate(request, username=username, password=pwd) #actually log in user
            if user is not None: #if they logged in then they are redirected to index. 
                login(request, user)
                return redirect('index')
            else:
                messages.success(request, ('There was an issue logging in. Please try again.'))
                return redirect('index')
        else:
            
            
            return render(request, 'mysite/login.html')

def register(request):
    context = {"items": items}
     # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
        
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')
        
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email = email
        )
        
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
        
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/tournament') #once they register it will take them to the tour home page
    return render(request, 'mysite/registerUser.html', context)

def logoutView(request):
    logout(request)
    return redirect('index')