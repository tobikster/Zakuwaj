from django.conf.urls.defaults import patterns, include, url
from words.views import index, wordsSetDetail, wordView

urlpatterns = patterns('words.views',
	url(r'^$', index.as_view(), name='words.words_sets_list'),
	url(r'^wordsset/(?P<pk>[0-9]+)/$', wordsSetDetail.as_view(), name='words.words_set_detail'),
	url(r'^wordsset/(?P<pk>[0-9]+)/learn$', wordView.as_view(), name='words.word_view'),
)
