from django.db import models

# Create your models here.

#missing id's...
class User(models.Model): 
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.DateTimeField("date it happens")

class Tournament_players(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE) #may to one, etc?

class Deck(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=65)
    desc = models.CharField(max_length=200)

class Cards(models.Model):
    deck = models.ForeignKey(Deck)
    name = models.CharField(max_length=65)
    desc = models.CharField(max_length=200)
    api_id = models.CharField(max_length=100)