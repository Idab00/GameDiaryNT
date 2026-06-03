from django.shortcuts import render, redirect
from .models import Game, GameLibrary,Genre

def landingview(request):
    return render(request, 'landingpage.html')

# Gamelist views
def gamelistview(request):
    gamelist = Game.objects.all()
    genrelist = Genre.objects.all()
    context = {'allgames': gamelist, 'genres': genrelist}
    return render(request, 'gamelist.html', context)

def addnewgame(request):
    a = request.POST['gametitle']
    b = request.POST['description']
    c = request.POST['releaseyear']
    d = request.FILES.get('cover')
    e = request.POST['genre']

    Game(gametitle = a, description = b, releaseyear = c,cover = d, genre = Genre.objects.get(id = e)).save()
    return redirect(request.META['HTTP_REFERER'])

def edit_game_get(request, id):
        game = Game.objects.get(id = id)
        genre = Genre.objects.all()
        context = {'game': game, 'genres': genre}
        return render (request,"edit_game.html",context)

def edit_game_post(request, id):
        game = Game.objects.get(id = id)
        game.releaseyear = request.POST['releaseyear']
        game.genre = Genre.objects.get(id=request.POST['genre'])
        game.description = request.POST['description']
        if 'cover' in request.FILES:
            game.cover = request.FILES['cover']

        game.save()
        return redirect(gamelistview)

def confirm_delete_game(request, id):
    game = Game.objects.get(id = id)
    context = {'game': game}
    return render (request,"confirmdelgame.html",context)


def delete_game(request, id):
    game = Game.objects.get(id = id)
    if game.cover:
         game.cover.delete(save=False)
    game.delete()
    return redirect(gamelistview)


# My library views

# Kirjautuneen käyttäjän oman pelikirjaston listaus filter metodilla
def mylibraryview(request):
    gamelib = GameLibrary.objects.filter(user=request.user)
    context = {'mylibrary': gamelib}
    return render(request, 'mylibrary.html', context)

def addgametolib(request, gameid):
    a = Game.objects.get(id=gameid)
    GameLibrary.objects.get_or_create(user = request.user ,game = a)
    return redirect('mylibrary/')