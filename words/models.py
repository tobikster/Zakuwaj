from django.db import models
from django.contrib.auth.models import User

#class User(models.Model):
#	login = models.CharField(max_length = 32)
#	name = models.CharField(max_length = 32)
#	email = models.EmailField()
#	description = models.TextField()
#	creationDate = models.DateTimeField(auto_now_add = True)

#class WordsUser(User):
#	description = models.TextField()

class WordsSet(models.Model):
	creator = models.ForeignKey(User)
	accessibility = models.CharField(max_length = 3, choices = (('prv', 'private'), ('pub', 'public')))
#	creationDate = models.DateTimeField(auto_now_add = True)

class Word(models.Model):
	word = models.CharField(max_length = 255)
	translation = models.CharField(max_length = 255)
	wordSet = models.ForeignKey(WordsSet)

class UserStatistic(models.Model):
	user = models.ForeignKey(User)

class Communicator(models.Model):
	communicator = models.CharField(max_length = 32)

class UserCommunicator(models.Model):
	user = models.ForeignKey(User)
	UID = models.CharField(max_length = 32)
	communicator = models.ForeignKey(Communicator)
