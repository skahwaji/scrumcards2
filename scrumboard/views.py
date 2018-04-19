from django.shortcuts import render
from .models import Card

def cards(request):
    #all_cards = Card.objects.all() #objects can be automatically detected but it will work fine
                                   #if you want to remoe the error message, add "python.linting.pylintArgs": ["--load-plugins=pylint_django"]

    all_cards  = Card.objects.cards_for_user(None)
    return render(request, "scrumboard/cards.html", 
    {'mycards': all_cards })