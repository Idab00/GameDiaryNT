from django.urls import path
from .views import landingview, gamelistview, mylibraryview, addnewgame, addtolibrary, edit_game_get, \
 edit_game_post, delete_game, confirm_delete_game, signup_post, signup_get, login_action, loginview, logout_action

urlpatterns = [
    path('', landingview),

    # Signup url's
    path('signup-post/', signup_post),
    path('signup-get/', signup_get),

    # Login and logout url's
    path('login-action/', login_action),
    path('login/', loginview),
    path('logout/', logout_action),

    # All games url's
    path('allgames/', gamelistview),
    path('add-game/', addnewgame),
    path('edit-game-post/<int:id>/', edit_game_post),
    path('edit-game-get/<int:id>/', edit_game_get),
    path('delete-game/<int:id>/', delete_game),
    path('confirm-delete-game/<int:id>/', confirm_delete_game),

    # My library url's
    path('mylibrary/', mylibraryview),
    path('add-to-library/', addtolibrary)
]
