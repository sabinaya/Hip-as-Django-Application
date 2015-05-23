from django.shortcuts import render
from django.http import HttpResponse

def game(request):
	context_dict = {'boldmessage': "I am the game"}

	return render(request, 'hip/game.html', context_dict)

