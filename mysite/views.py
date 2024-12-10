from django.shortcuts import render
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

items = menu_items.objects.all() #grab the menu items to be used within this file

def index(request): #home/login page
    card_collection = Card.objects.all() #.all is what made this work and grab all cards
    context = {"collection": card_collection, "items": items}
    return render(request, "mysite/index.html", context)

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
        return redirect('/register/')
    return render(request, 'mysite/registerUser.html', context)