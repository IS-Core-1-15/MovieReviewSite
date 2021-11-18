from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.templatetags.static import static
import os
from .models import *

# Create your views here.
# List all the movies in the DB
def indexPageView(request):
    movies = Movie.objects.all()
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + '/photos')
    context = {
        'movielist': movies,
        'image': img_list[0]
    }
    return render(request, 'crudmovies/index.html', context)

# show single movie info
def moviePageView(request, movieTitle):
    movie = Movie.objects.filter(title=movieTitle)
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + '/photos')

    context = {
        'movie': movie[0],
        'image': img_list[0]
    }

    return render(request, 'crudmovies/single.html', context)

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


def editReviewView(request) :
    return HttpResponse('Edit Review')


def deleteMovieView(request) :
    return HttpResponse('Delete Movie')


def deleteReviewView(request) :
    return HttpResponse('Delete Review')


def editMoviePageView(Request):
    return HttpResponse('editMoviePageView')


def addMoviePageView(request):
    return HttpResponse('addMoviePageView')


def addReviewPageView(request, movieID):
    return HttpResponse('addReviewPageView')