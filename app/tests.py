from django.test import TestCase
from django.contrib.auth.models import User
from app.models import Game, Genre

class UserTest(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(
            username="testi3",
            password="salasana123"
        )

        self.assertEqual(user.username, "testi3")

class GameTest(TestCase):

    def test_game_creation(self):
        genre = Genre.objects.create(name="RPG")

        game = Game.objects.create(
            gametitle="Skyrim",
            releaseyear=2011,
            genre=genre
        )

        self.assertEqual(game.gametitle, "Skyrim")
