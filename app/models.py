from django.contrib.auth.models import User
from django.db import models

# Pelin genre   
class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
# Peli
class Game(models.Model):
    gametitle = models.CharField(max_length=200, default="game")
    description = models.TextField()
    releaseyear = models.PositiveIntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to="covers/", blank=True, null=True)

    def __str__(self):
        return self.gametitle
    
# Pelikirjasto  
class GameLibrary(models.Model):
    STATUS_CHOICES = [
        ("owned", "Owned"),
        ("playing", "Playing"),
        ("completed", "Completed"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="owned")

    class Meta:
        unique_together = ("user", "game")