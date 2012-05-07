from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required
from words.views import index, wordsSetDetail, wordView

urlpatterns = patterns('words.views',
	url(r'^$', 'index', name='words.words_sets_list'),
	url(r'^wordsset/(?P<wordsSetId>[0-9]+)/$', 'wordsSetDetail', name='words.words_set_detail'),
	url(r'^learn/(?P<wordsSetId>[0-9]+)/$', 'wordView', name='words.word_view'),
)
