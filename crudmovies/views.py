from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
# List all the movies in the DB
def indexPageView(request):
    movies = Movie.objects.all()
    context = {
        'movielist': movies
    }
    return render(request, 'crudmovies/index.html', context)

# show single movie info
def moviePageView(request, movieTitle):
    movie = Movie.objects.filter(title=movieTitle)

    context = {
        'movie': movie
    }

    return render(request, 'crudmovies/single.html', context)

def searchPageView(request):
    return HttpResponse('Search')


def listPageView(request):
    return HttpResponse('List')


def editReviewView(request) :
    return HttpResponse('Edit Review')


def deleteMovieView(request) :
    return HttpResponse('Delete Movie')


def deleteReviewView(request) :
    return HttpResponse('Delete Review')


def aboutPageView(Request):
    return HttpResponse('About')


def editMoviePageView(Request):
    return HttpResponse('editMoviePageView')


def addMoviePageView(request):
    return HttpResponse('addMoviePageView')


def addReviewPageView(request, movieID):
    return HttpResponse('addReviewPageView')