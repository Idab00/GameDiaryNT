from django.contrib import admin

from app.models import Game, Genre, GameLibrary


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass

@admin.register(GameLibrary)
class GameLibraryAdmin(admin.ModelAdmin):
    pass


