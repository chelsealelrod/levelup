from django.db import models

class Event(models.Model):
    game = models.ForeignKey("levelupapi.Game",
        on_delete=models.DO_NOTHING)
    organizer = models.ForeignKey("levelupapi.Gamer",
        on_delete=models.DO_NOTHING, null=True)
    description = models.CharField(max_length=50)
    date = models.DateTimeField(max_length=10)
    time = models.TimeField(auto_now_add=True)
    attendees = models.ManyToManyField("levelupapi.Gamer",
        related_name="attending")
    
    
    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value