# -*- coding: utf-8 -*-
# -247
# 282
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from words.models import WordsSet, Word
import random

@login_required
def index(request):
	wordSets = []
	if request.user.is_authenticated():
		for userWordSet in WordsSet.objects.filter(creator = request.user.pk):
			wordSets.append(userWordSet)
	for wordSet in WordsSet.objects.filter(accessibility = 'pub'):
		if wordSet not in wordSets:
			wordSets.append(wordSet)
	
	return render_to_response('words/index.html', {'wordsset_list': wordSets}, context_instance = RequestContext(request))

@login_required
def wordsSetDetail(request, wordsSetId):
	wordSet = get_object_or_404(WordsSet, pk = wordsSetId)
	if wordSet.accessibility == 'prv' and wordSet.creator != request.user:
		wordSet = None

	return render_to_response('words/wordsSetDetail.html', {'wordsSet': wordSet}, context_instance = RequestContext(request))

@login_required
def wordView(request, wordsSetId):
	if 'clear' in request.GET:
		if 'word' in request.session:
			del request.session['word']

	if 'word' not in request.session:
		request.session['word'] = {
			'probabilities': {},
			'currentWordId': -1,
		}

	print 'Przed:'
	print request.session['word']

	if 'word' in request.session:
		if 'reset' in request.GET or 'probabilities' not in request.session['word']:
			request.session['word']['probabilities'] = {}
			request.session['word']['currentWordId'] = -1
			for word in get_object_or_404(WordsSet, pk = wordsSetId).word_set.all():
				request.session['word']['probabilities'][word.pk] = 1.0
		if 'currentWordId' in request.session['word']:
			print 'request.GET:', request.GET
			print 'request.session["word"]["currentWordId"]:', request.session['word']['currentWordId']
			if 'answer' in request.GET and request.session['word']['currentWordId'] != -1:
				probability = request.session['word']['probabilities'][request.session['word']['currentWordId']]
				if request.GET['answer'] == 'good':
					probability = probability * 0.8
				elif request.GET['answer'] == 'avg':
					probability = probability * 1.05
				elif request.GET['answer'] == 'bad':
					probability = probability * 1.2
				print 'probability:', probability
				request.session['word']['probabilities'][request.session['word']['currentWordId']] = probability
			else:
				request.session['word']['currentWordId'] = -1
		if 'probabilities' in request.session['word']:
			probabilitySum = 0.0
			for prob in request.session['word']['probabilities'].viewvalues():
				probabilitySum = probabilitySum + prob
			rand = random.uniform(0, probabilitySum)
			request.session['word']['currentWordId'] = -1
			for (wordId, prob) in request.session['word']['probabilities'].viewitems():
				rand = rand - prob
				if rand <= 0.0:
					request.session['word']['currentWordId'] = wordId
					break
	word = get_object_or_404(Word, pk = request.session['word']['currentWordId'])
	print 'Po:'
	print request.session['word']
	request.session.modified = True
	return render_to_response('words/wordDetail.html', {'word': word}, context_instance = RequestContext(request))

#@login_required
#def wordView(request, wordsSetId):
#	# TODO: To trzeba będzie usunąć!
#	if 'clear' in request.GET:
#		del request.session['word']
#
#	if 'reset' in request.GET or 'words' not in request.session:
#		try:
#			del request.session['words']
#		except KeyError:
#			pass
#		words = {}
#		for word in get_object_or_404(WordsSet, pk = wordsSetId).word_set.all():
#			words[word.pk] = 1.0
#		request.session['words'] = words
#
#	print request.session['words']
#	if 'currentWordId' in request.session:
#		if 'answer' in request.GET:
#			probability = request.session['words'][request.session['currentWordId']]
#			if request.GET['answer'] == 'good':
#				probability = probability * 0.1
#			elif request.GET['answer'] == 'avg':
#				pass
#			elif request.GET['answer'] == 'bad':
#				probability = probability * 5.0
#			request.session['words'][request.session['currentWordId']] = probability
#		else:
#			del request.session['currentWordId']
#
#	try:
##		probabilitySum = 0.0
#		for prob in request.session['words'].viewvalues():
#			probabilitySum += prob
#		rand = random.uniform(0, probabilitySum)
#		for (wordId, prob) in request.session['words'].viewitems():
#			rand -= prob
#			if rand <= 0:
#				resultId = wordId
#				request.session['currentWordId'] = resultId
#				break
#		else:
#			resultId = -1 #Wyjatek!
#	except KeyError:
#		pass
#
#	word = get_object_or_404(Word, pk = resultId)
#	return render_to_response('words/wordDetail.html', {'word': word}, context_instance = RequestContext(request))
