from django.urls import path
from .views import landingview, gamelistview, mylibraryview, addnewgame, addgametolib, edit_game_get, edit_game_post, \
delete_game, confirm_delete_game

urlpatterns = [
    path('', landingview),

    # All games url's
    path('allgames/', gamelistview),
    path('add-game/', addnewgame),
    path('edit-game-post/<int:id>/', edit_game_post),
    path('edit-game-get/<int:id>/', edit_game_get),
    path('delete-game/<int:id>/', delete_game),
    path('confirm-delete-game/<int:id>/', confirm_delete_game),

    # My library url's
    path('mylibrary/', mylibraryview),
    path('add-gametolib/', addgametolib), 
]
