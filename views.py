from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	if 'word' in request.session:
		print '"word" from index =', request.session['word']
	return render_to_response('index.html', context_instance = RequestContext(request))
