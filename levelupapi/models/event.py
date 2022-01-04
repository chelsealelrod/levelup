from django.db import models

class Event(models.Model):
    
    title = models.CharField(max_length=55)
    game = models.ForeignKey("levelupapi.Game",
        on_delete=models.CASCADE)
    gamer = models.ForeignKey("levelupapi.Gamer",
        on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    date = models.DateTimeField(max_length=10)
    time = models.TimeField(auto_now_add=True)
    attendees = models.ManyToManyField("levelupapi.Gamer",
        related_name="myevents")
    