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
	if 'words' not in request.session or 'reset' in request.GET:
		try:
			del request.session['words']
		except KeyError:
			pass

		words = []	
		for word in get_object_or_404(WordsSet, pk = wordsSetId).word_set.all():
			words.append((word.pk, 1.0))
		
		request.session['words'] = words

	try:
		probabilitySum = 0.0
		for (wordId, prob) in request.session['words']:
			probabilitySum += prob

		rand = random.uniform(0, probabilitySum)
		for (wordId, prob) in request.session['words']:
			rand -= prob
			if rand <= 0:
				resultId = wordId
				break
		else:
			resultId = -1 #Wyjatek!
	except KeyError:
		pass

	word = get_object_or_404(Word, pk = resultId)
	return render_to_response('words/wordDetail.html', {'word': word}, context_instance = RequestContext(request))
