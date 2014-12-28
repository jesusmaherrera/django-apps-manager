from django.db import models
from django.contrib.auth.models import User

class Application(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Business(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Server(models.Model):	
    user = models.ForeignKey(User)
    business = models.ForeignKey('Business')
    ubicacion = models.CharField(max_length=200)
    aplications = models.ManyToManyField('Application')

    def __str__(self):
        return u'%s-%s'%(self.business, self.ubicacion)