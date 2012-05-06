from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from words.models import WordsSet

class index(ListView):
	model = WordsSet
	template_name = 'words/index.html'
	
class wordsSetDetail(DetailView):
	context_object_name = 'wordsSet'
	model = WordsSet
	template_name = 'words/wordsSetDetail.html'
	
@login_required
def wordView(request, wordsSetId, previousWord = None, modify = 1.0):
	if previousWord != None:
		pass
	
	word = get_object_or_404(WordsSet, pk = wordsSetId).getRandomWord()
	return render_to_response('words/wordDetail.html', {'word': word})
