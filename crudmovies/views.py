from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def indexPageView(request):
    movies = Movie.objects.all()
    print(movies[0])
    context = {
        'movielist': movies
    }
    return render(request, 'crudmovies/review.html', context)


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


def movieInfoPageView(request, movieID):
    return HttpResponse('MovieInfoPageView')


def addMoviePageView(request):
    return HttpResponse('addMoviePageView')


def addReviewPageView(request, movieID):
    return HttpResponse('addReviewPageView')