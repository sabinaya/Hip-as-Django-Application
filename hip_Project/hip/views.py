from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context,loader,RequestContext
from hip.models import board


def game(request):
	context_dict = {}

	if request.POST:
		if 'Start' in request.POST.keys():

			gameBoard = board.objects.get(player="none")
			gameBoard.root_Board()

			context_dict['img1'] = gameBoard.img1
			context_dict['img2'] = gameBoard.img2
			context_dict['img3'] = gameBoard.img3
			context_dict['img4'] = gameBoard.img4
			context_dict['img5'] = gameBoard.img5
			context_dict['img6'] = gameBoard.img6
			context_dict['img7'] = gameBoard.img7
			context_dict['img8'] = gameBoard.img8
			context_dict['img9'] = gameBoard.img9
			context_dict['game_over'] = gameBoard.game_over

			return render(request, 'hip/game.html', context_dict)

		if '1' in request.POST.keys():
			
			gameBoard = board.objects.get(player="Human")
			gameBoard.img1 = 1
			gameBoard.save()
			gameBoard.root_Board()

			context_dict['img1'] = gameBoard.img1
			context_dict['img2'] = gameBoard.img2
			context_dict['img3'] = gameBoard.img3
			context_dict['img4'] = gameBoard.img4
			context_dict['img5'] = gameBoard.img5
			context_dict['img6'] = gameBoard.img6
			context_dict['img7'] = gameBoard.img7
			context_dict['img8'] = gameBoard.img8
			context_dict['img9'] = gameBoard.img9
			context_dict['game_over'] = gameBoard.game_over


			return render(request, 'hip/game.html', context_dict)

		if '2' in request.POST.keys():
			
			gameBoard = board.objects.get(player="Human")
			gameBoard.img2 = 1
			gameBoard.save()
			gameBoard.root_Board()

			context_dict['img1'] = gameBoard.img1
			context_dict['img2'] = gameBoard.img2
			context_dict['img3'] = gameBoard.img3
			context_dict['img4'] = gameBoard.img4
			context_dict['img5'] = gameBoard.img5
			context_dict['img6'] = gameBoard.img6
			context_dict['img7'] = gameBoard.img7
			context_dict['img8'] = gameBoard.img8
			context_dict['img9'] = gameBoard.img9
			context_dict['game_over'] = gameBoard.game_over


			return render(request, 'hip/game.html', context_dict)

		if '3' in request.POST.keys():
			
			gameBoard = board.objects.get(player="Human")
			gameBoard.img3 = 1
			gameBoard.save()
			gameBoard.root_Board()

			context_dict['img1'] = gameBoard.img1
			context_dict['img2'] = gameBoard.img2
			context_dict['img3'] = gameBoard.img3
			context_dict['img4'] = gameBoard.img4
			context_dict['img5'] = gameBoard.img5
			context_dict['img6'] = gameBoard.img6
			context_dict['img7'] = gameBoard.img7
			context_dict['img8'] = gameBoard.img8
			context_dict['img9'] = gameBoard.img9
			context_dict['game_over'] = gameBoard.game_over


			return render(request, 'hip/game.html', context_dict)

		if '4' in request.POST.keys():
			
			gameBoard = board.objects.get(player="Human")
			gameBoard.img4 = 1
			gameBoard.save()
			gameBoard.root_Board()

			context_dict['img1'] = gameBoard.img1
			context_dict['img2'] = gameBoard.img2
			context_dict['img3'] = gameBoard.img3
			context_dict['img4'] = gameBoard.img4
			context_dict['img5'] = gameBoard.img5
			context_dict['img6'] = gameBoard.img6
			context_dict['img7'] = gameBoard.img7
			context_dict['img8'] = gameBoard.img8
			context_dict['img9'] = gameBoard.img9
			context_dict['game_over'] = gameBoard.game_over


			return render(request, 'hip/game.html', context_dict)

		if '5' in request.POST.keys():
			
			gameBoard = board.objects.get(player="Human")
			gameBoard.img5 = 1
			gameBoard.save()
			gameBoard.root_Board()

			context_dict['img1'] = gameBoard.img1
			context_dict['img2'] = gameBoard.img2
			context_dict['img3'] = gameBoard.img3
			context_dict['img4'] = gameBoard.img4
			context_dict['img5'] = gameBoard.img5
			context_dict['img6'] = gameBoard.img6
			context_dict['img7'] = gameBoard.img7
			context_dict['img8'] = gameBoard.img8
			context_dict['img9'] = gameBoard.img9
			context_dict['game_over'] = gameBoard.game_over


			return render(request, 'hip/game.html', context_dict)

		if '6' in request.POST.keys():
			
			gameBoard = board.objects.get(player="Human")
			gameBoard.img6 = 1
			gameBoard.save()
			gameBoard.root_Board()

			context_dict['img1'] = gameBoard.img1
			context_dict['img2'] = gameBoard.img2
			context_dict['img3'] = gameBoard.img3
			context_dict['img4'] = gameBoard.img4
			context_dict['img5'] = gameBoard.img5
			context_dict['img6'] = gameBoard.img6
			context_dict['img7'] = gameBoard.img7
			context_dict['img8'] = gameBoard.img8
			context_dict['img9'] = gameBoard.img9
			context_dict['game_over'] = gameBoard.game_over


			return render(request, 'hip/game.html', context_dict)

		if '7' in request.POST.keys():
			
			gameBoard = board.objects.get(player="Human")
			gameBoard.img7 = 1
			gameBoard.save()
			gameBoard.root_Board()

			context_dict['img1'] = gameBoard.img1
			context_dict['img2'] = gameBoard.img2
			context_dict['img3'] = gameBoard.img3
			context_dict['img4'] = gameBoard.img4
			context_dict['img5'] = gameBoard.img5
			context_dict['img6'] = gameBoard.img6
			context_dict['img7'] = gameBoard.img7
			context_dict['img8'] = gameBoard.img8
			context_dict['img9'] = gameBoard.img9
			context_dict['game_over'] = gameBoard.game_over


			return render(request, 'hip/game.html', context_dict)

		if '8' in request.POST.keys():
			
			gameBoard = board.objects.get(player="Human")
			gameBoard.img8 = 1
			gameBoard.save()
			gameBoard.root_Board()

			context_dict['img1'] = gameBoard.img1
			context_dict['img2'] = gameBoard.img2
			context_dict['img3'] = gameBoard.img3
			context_dict['img4'] = gameBoard.img4
			context_dict['img5'] = gameBoard.img5
			context_dict['img6'] = gameBoard.img6
			context_dict['img7'] = gameBoard.img7
			context_dict['img8'] = gameBoard.img8
			context_dict['img9'] = gameBoard.img9
			context_dict['game_over'] = gameBoard.game_over


			return render(request, 'hip/game.html', context_dict)

		if '9' in request.POST.keys():
			
			gameBoard = board.objects.get(player="Human")
			gameBoard.img9 = 1
			gameBoard.save()
			gameBoard.root_Board()

			context_dict['img1'] = gameBoard.img1
			context_dict['img2'] = gameBoard.img2
			context_dict['img3'] = gameBoard.img3
			context_dict['img4'] = gameBoard.img4
			context_dict['img5'] = gameBoard.img5
			context_dict['img6'] = gameBoard.img6
			context_dict['img7'] = gameBoard.img7
			context_dict['img8'] = gameBoard.img8
			context_dict['img9'] = gameBoard.img9
			context_dict['game_over'] = gameBoard.game_over


			return render(request, 'hip/game.html', context_dict)

	return render(request, 'hip/game.html')




