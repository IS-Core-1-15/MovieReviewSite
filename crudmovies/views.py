from django.shortcuts import redirect, render
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
                'movie': movie
            }

        return render(request, 'crudmovies/addmovie.html', context)


def deleteMoviePageView(request, movie_title, movie_year):
    # return HttpResponse("You are trying to delete the movie " + movie_title + " produced in " + movie_year
    # + " . Nothing actually happened.")

    movieToDelete = Movie.objects.get(
        title=movie_title, release_year=movie_year)
    movieToDelete.delete()

    return redirect('index')


def saveMoviePageView(request):
    id = request.POST['movie']
    s = searchMovie(id)
    movie = Movie.create(s)
    movie.save()

    return redirect('index')


def joinusPageView(request):
    return render(request, 'crudmovies/joinus.html')


def aboutPageView(request):
    return render(request, 'crudmovies/about.html')


def contactPageView(request):
    return render(request, 'crudmovies/contact.html')


def searchPageView(request):
    key = request.POST['key']
    form = request.POST
    if 'key' in request.POST:
        key = request.POST['key']
        movies = Movie.objects.filter(title__contains=key)
        context = {
            'movielist': movies,
        }
    else:
        key = False
        msg = f'Sorry we could not find any movie with that name'

    context['msg'] = msg

    return render(request, 'crudmovies/index.html', context)


def listPageView(request):
    return HttpResponse('List')


def editReviewView(request):
    return render(request, 'crudmovies/editreview.html')


def deleteReviewView(request):
    return HttpResponse('Delete Review')


def editMoviePageView(Request):
    return HttpResponse('editMoviePageView')


def addReviewPageView(request, movieID):
    return HttpResponse('addReviewPageView')
