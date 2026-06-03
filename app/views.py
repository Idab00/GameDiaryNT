from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Game, GameLibrary, Genre

def landingview(request):
    return render(request, 'landingpage.html')

# Signup action
def signup_get(request):
    return render(request, "signup.html")

def signup_post(request):
    if request.POST["password"] != request.POST["password2"]:
         return render( request, "signup.html", {"error": "Passwords do not match"})
    username = request.POST["username"]
    password = request.POST["password"]
    
    email = request.POST["email"]
    User.objects.create_user(username=username, password=password, email=email)
    return redirect(landingview)

# Login action
def loginview(request):
    return render(request, "login.html")

def login_action(request):
    user = request.POST['username']
    password = request.POST['password']
    # Löytyykö kyseistä käyttäjää?
    user = authenticate(username = user, password = password)
    #Jos löytyy:
    if user:
        # Kirjataan sisään
        login(request, user)
        context = {'name': user.first_name}
        # Kutsutaan suoraan landingview.html
        return render(request,'landingpage.html',context)
    # Jos ei kyseistä käyttäjää löydy
    else:
        return render(request, 'loginerror.html')

# Logout action
def logout_action(request):
    logout(request)
    return render(request, 'landingpage.html')

# Gamelist views
def gamelistview(request):
    
        gamelist = Game.objects.all()
        genrelist = Genre.objects.all()
        context = {'allgames': gamelist, 'genres': genrelist}
        return render(request, 'gamelist.html', context)

def addnewgame(request):
    if not request.user.is_authenticated:
        return render(request, 'gamelist.html')
    else:
        a = request.POST['gametitle']
        b = request.POST['description']
        c = request.POST['releaseyear']
        d = request.FILES.get('cover')
        e = request.POST['genre']
        Game(gametitle = a, description = b, releaseyear = c,cover = d, genre = Genre.objects.get(id = e)).save()
        return redirect(request.META['HTTP_REFERER'])

def edit_game_get(request, id):
    if not request.user.is_authenticated:
        return render(request, 'gamelist.html')
    else:
        game = Game.objects.get(id = id)
        genre = Genre.objects.all()
        context = {'game': game, 'genres': genre}
        return render (request,"edit_game.html",context)

def edit_game_post(request, id):
    if not request.user.is_authenticated:
        return render(request, 'gamelist.html')
    else:
        game = Game.objects.get(id = id)
        game.releaseyear = request.POST['releaseyear']
        game.genre = Genre.objects.get(id=request.POST['genre'])
        game.description = request.POST['description']
        if 'cover' in request.FILES:
            game.cover = request.FILES['cover']

        game.save()
        return redirect(gamelistview)

def confirm_delete_game(request, id):
    if not request.user.is_authenticated:
        return render(request, 'gamelist.html')
    else:
        game = Game.objects.get(id = id)
        context = {'game': game}
        return render (request,"confirmdelgame.html",context)


def delete_game(request, id):
    if not request.user.is_authenticated:
        return render(request, 'gamelist.html')
    else:
        game = Game.objects.get(id = id)
        if game.cover:
            game.cover.delete(save=False)
        game.delete()
        return redirect(gamelistview)


# My library views

# Kirjautuneen käyttäjän oman pelikirjaston listaus filter metodilla
def mylibraryview(request):
    if not request.user.is_authenticated:
        return render(request, 'landingpage.html')
    else:
        gamelib = GameLibrary.objects.filter(user=request.user)
        context = {'mylibrary': gamelib, 'games': Game.objects.all()}
        return render(request, 'mylibrary.html', context)
    

def addtolibrary(request):
    if not request.user.is_authenticated:
        return render(request, 'landingpage.html')
    else:
        a = Game.objects.get(id=request.POST["gameid"])
        GameLibrary.objects.get_or_create(user = request.user ,game = a)
        return redirect('/mylibrary/')