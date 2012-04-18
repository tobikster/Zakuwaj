from words.models import UserStatistic, WordsSet, Word, Communicator, UserCommunicator
from django.contrib import admin

class WordsInline(admin.StackedInline):
	model = Word
	extra = 1

class WordsSetAdmin(admin.ModelAdmin):
	fieldsets = [
		('Autor', {'fields': ['creator']}),
		('Dostepnosc', {'fields': ['accessibility']}),
		('Nazwa', {'fields': ['name']}),
		('Język źródłowy', {'fields': ['sourceLanguage']}),
		('Język docelowy', {'fields': ['destinationLanguage']}),
	]
	inlines = [WordsInline]

admin.site.register(UserStatistic)
admin.site.register(WordsSet, WordsSetAdmin)
admin.site.register(Word)
admin.site.register(Communicator)
admin.site.register(UserCommunicator)
