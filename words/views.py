from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import ListView, DetailView
from words.models import WordsSet, Word

def index(request):
	return render_to_response('words/index.html')

class index(ListView):
	model = WordsSet
	template_name = 'words/index.html'
	
class wordsSetDetail(DetailView):
	context_object_name = 'wordsSet'
	model = WordsSet
	template_name = 'words/wordsSetDetail.html'
	
def wordView(request, wordsSetId):
	word = get_object_or_404(WordsSet, pk = wordsSetId).getRandomWord
	return render_to_response('words/wordDetail.html', {'word': word})