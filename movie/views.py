from django.shortcuts import render
from .models import Movie, Genre
from django.http import HttpResponse, Http404

def home(request):
    movies = Movie.objects.all()
    data = {
        "movies":movies
    }
    return render(request, 'home.html', data)

def detail(request, pk):
    try:
        movie = Movie.objects.get(id=pk)
        data = {
            "movie": movie
        }
        return render(request, 'detail.html', data)
    except Movie.DoesNotExist:
        raise Http404("Movie not found")