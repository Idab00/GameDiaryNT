from django.shortcuts import render

def landingview(request):
    return render(request, 'landingpage.html')

def gamelistview(request):
    return render(request, 'gamelist.html')

def librarylistview(request):
    return render(request, 'librarylist.html')