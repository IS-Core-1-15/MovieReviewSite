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
    context = {
        'movielist': movies,
    }
    return render(request, 'crudmovies/index.html', context)

# show single movie info
def moviePageView(request, movieTitle, director):
    movie = Movie.objects.filter(title=movieTitle, director=director)
    reviews = Review.objects.filter(movie_id=movie[0].id)

    context = {
        'movie': movie[0],
        'reviews' : reviews
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


def deleteReviewView(request) :
    return HttpResponse('Delete Review')


def editMoviePageView(Request):
    return HttpResponse('editMoviePageView')


def addReviewPageView(request, movieID):
    return HttpResponse('addReviewPageView')