from django.db import models
from django.contrib.auth.models import User

class WordsSet(models.Model):
	name = models.CharField(max_length = 50)
	sourceLanguage = models.CharField(max_length = 50)
	destinationLanguage = models.CharField(max_length = 50)
	creator = models.ForeignKey(User)
	accessibility = models.CharField(max_length = 3, choices = (('prv', 'private'), ('pub', 'public')))
	creationDate = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return self.name + ': [' + self.sourceLanguage + ' -> ' + self.destinationLanguage +']'
	
	def getName(self):
		return self.name
	
	def getWords(self):
		return self.word_set
		
	def getRandomWord(self):
		return self.word_set.order_by('?')[0]

class Word(models.Model):
	word = models.CharField(max_length = 255)
	translation = models.CharField(max_length = 255)
	probability = models.DecimalField(max_digits = 3, decimal_places = 2)
	wordSet = models.ForeignKey(WordsSet)
	
	def __unicode__(self):
		return self.word + ' -> ' + self.translation
	
	def getWord(self):
		return self.word
	
	def getTranslation(self):
		return self.translation

class UserStatistic(models.Model):
	user = models.ForeignKey(User)

class Communicator(models.Model):
	communicator = models.CharField(max_length = 32)
	
	def __unicode__(self):
		return self.communicator

class UserCommunicator(models.Model):
	user = models.ForeignKey(User)
	UID = models.CharField(max_length = 32)
	communicator = models.ForeignKey(Communicator)
