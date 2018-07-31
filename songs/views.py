import random
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound 
from django.db.models import Q
from .models import Music_data
# Create your views here.

def home(request):
	return render(request,'songs/musicSuggestion.html')

def suggestion(request):
	
	if request.method ==	'GET':
		artist = request.GET['artist']
		from_date = request.GET['from_date']
		# from_date = int(from_date)
		to_date = request.GET['to_date']
		# to_date = int(to_date)
		genre = request.GET['genre']

		song=Music_data.objects.filter(
			Q(artist__icontains=artist)and
			Q(release_date=None) and
			Q(genre__icontains=genre)
			)
		try:
			for date in range(int(from_date),int(to_date)+1):
				for i in enumerate(song):
					if song.release_date == date:
						songs[i]=song[i]
		except:
			pass

	if song:
		random_song = random.choice(song)
	else:

		random_song = Music_data.objects.order_by('?').first()
	# else:
	# 	return redirect( 'songs/musicSuggestion.html')
	return render(request,'songs/musicSuggestion.html', {'random_song':random_song})
