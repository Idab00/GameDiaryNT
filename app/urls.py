from django.urls import path
from .views import landingview, gamelistview, mylibraryview, addnewgame, addgametolib, searchgame

urlpatterns = [
    path('', landingview),

    # All games url's
    path('allgames/', gamelistview),
    path('add-game/', addnewgame),
    path('search-game/', searchgame),

    # My library url's
    path('mylibrary/', mylibraryview),
    path('add-gametolib/', addgametolib), 
]
