from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .api.imdb import searchMovie
from django.templatetags.static import static
import os
from .models import *

# Create your views here.
# List all the movies in the DB


def indexPageView(request):
    movies = Movie.objects.all()
    context = {
        'movielist': movies,
    }
    return render(request, 'crudmovies/index.html', context)

# show single movie info


def moviePageView(request, movieTitle, movieYear):
    movie = Movie.objects.filter(title=movieTitle, release_year=movieYear)
    # reviews = Review.objects.filter(movie_id=movie[0].id)

    context = {
        'movie': movie[0],
        # 'reviews' : reviews
    }

    return render(request, 'crudmovies/single.html', context)


def addPageView(request):
    if request.method == 'GET':
        return render(request, 'crudmovies/addmovie.html')
    elif request.method == 'POST':
        key = request.POST['title']
        movie = searchMovie(key)

        if movie.title == '':
            context = {
                'msg': 'We could not find your movie, try another one!'
            }
        else:
            context = {
                'msg': 'Is this the movie you\'re looking for?',
                'msg2': 'If not, make sure it is spelled correctly or try searching for a different movie',
                'movie': movie
            }
        for attr, value in movie.__dict__.items():
            print(f"{attr}: {value}")
        return render(request, 'crudmovies/addmovie.html', context)


def deleteMoviePageView(request):
    return render(request, 'crudmovies/addmovie.html')


def joinusPageView(request):
    return render(request, 'crudmovies/joinus.html')


def aboutPageView(request):
    return render(request, 'crudmovies/about.html')


def contactPageView(request):
    return render(request, 'crudmovies/contact.html')


def searchPageView(request):
    return HttpResponse('Search')


def listPageView(request):
    return HttpResponse('List')


def editReviewView(request):
    return HttpResponse('Edit Review')


def deleteReviewView(request):
    return HttpResponse('Delete Review')


def editMoviePageView(Request):
    return HttpResponse('editMoviePageView')


def addReviewPageView(request, movieID):
    return HttpResponse('addReviewPageView')
