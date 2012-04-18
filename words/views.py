from django.shortcuts import render_to_response
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
	
class wordView(DetailView):
	context_object_name = 'word'
	model = Word
	template_name = 'words/wordDetail.html'