from django.urls import path
from .views import landingview, gamelistview, mylibraryview, addnewgame, addgametolib

urlpatterns = [
    path('', landingview),

    # All games url's
    path('allgames/', gamelistview),
    path('add-game/', addnewgame),

    # My library url's
    path('mylibrary/', mylibraryview),
    path('add-gametolib/', addgametolib), 
]
