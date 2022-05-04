from django.db import models

# Create your models here.

class TurnLight(models.Model):
    name = models.TextField()
    state = models.BooleanField()
    stateint = models.PositiveSmallIntegerField(default=1)
    ip = models.TextField(null= True)
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class meta():
        ordering = ['-updated']

class CardModel(models.Model):
    cardCode = models.TextField()

    def __str__(self):
        return self.cardCode

    class meta():
        ordering = ['-updated']


