from django.db import models

# Create your models here.
class Medecins(models.Model):
    noms=models.CharField(max_length=255)
    specialite=models.CharField(max_length=255)
    contact=models.IntegerField()

class Article(models.Model):
    titre=models.CharField(max_length=255)
    date=models.DateField()
    contenu=models.TextField()

class Service(models.Model):
    titre=models.CharField(max_length=255)
    image=models.ImageField()
    description=models.TextField()

class Administration(models.Model):
    titre=models.CharField(max_length=255)
    image=models.ImageField()
    description=models.TextField()


class decouvrir(models.Model):
    titre=models.CharField(max_length=255)
    image=models.ImageField()
    messages=models.TextField()



class contact(models.Model):
    noms=models.CharField(max_length=255)
    mail=models.EmailField()
    description=models.TextField()

class Partenaire(models.Model):
    titre=models.CharField(max_length=255)
    description=models.TextField()


