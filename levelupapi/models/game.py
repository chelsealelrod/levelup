from django.db import models


class Game(models.Model):

    title = models.CharField(max_length=55)
    maker = models.CharField(max_length=55)
    gamer = models.ForeignKey("levelupapi.Gamer",
            on_delete=models.CASCADE)
    game_type = models.ForeignKey("levelupapi.GameType",
            on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()
    