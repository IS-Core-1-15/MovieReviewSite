from django.db.models import Avg
from django.db.models.base import ModelStateFieldsCacheDescriptor
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


def moviePageView(request, movieID):
    movie = Movie.objects.get(movie_id=movieID)
    reviews = Review.objects.filter(movie_id=movie.movie_id)

    context = {
        'movie': movie,
        'reviews': reviews,
        'count' : len(reviews),
    }

    if len(reviews) > 0 :
        avg = reviews.aggregate(Avg('rating'))
        avgRating = int((avg['rating__avg']/5)*100)
        context['rating'] = avgRating
    else :
        msg = 'No reviews yet'
        context['msg'] = msg

    return render(request, 'crudmovies/single.html', context)


def addPageView(request):
    if request.method == 'GET':
        return render(request, 'crudmovies/addmovie.html')
    elif request.method == 'POST':
        key = request.POST['title']
        movie = searchMovie(key)
        try:
            check = Movie.objects.get(imdbid=movie.imdbid)
        except Exception as e:
            print(e)
            check = False
            
        if check:
            return redirect('moviePageView', movieID=check.movie_id)

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


def aboutPageView(request):
    return render(request, 'crudmovies/about.html')


def searchPageView(request):
    key = request.POST['key'].title()
    form = request.POST
    if 'key' in request.POST:
        key = request.POST['key'].title()
        movies = Movie.objects.filter(title__icontains=key)
        context = {
            'movielist': movies,
        }
    else:
        key = False
        msg = f'Sorry we could not find any movie with that name'

    return render(request, 'crudmovies/index.html', context)


def listPageView(request):
    return HttpResponse('List')


def editReviewView(request, review_id):
    data = Review.objects.get(review_id=review_id)

    context = {
        "record": data
    }
    return render(request, 'crudmovies/editreview.html', context)


def editExistingReview(request):
    from datetime import date
    if request.method == 'POST':
        review_id = request.POST['review_id']

        review = Review.objects.get(review_id=review_id)

        review.username = request.POST['username']
        review.rating = request.POST['rating']
        review.description = request.POST['description']
        review.review_date = date.today()

        review.save()

        return redirect(moviePageView, review.movie_id)


def deleteReviewView(request, review_id):
    review = Review.objects.get(review_id=review_id)
    movie = review.movie_id
    review.delete()

    return redirect('moviePageView', movieID=movie)


def editMoviePageView(request, movie_id):
    data = Movie.objects.get(movie_id=movie_id)

    context = {
        "record": data
    }

    return render(request, 'crudmovies/editmovie.html', context)


def editExistingMovie(request):
    if request.method == 'POST':
        movie_id = request.POST['movie_id']

        movie = Movie.objects.get(movie_id=movie_id)

        movie.title = request.POST['title']
        movie.imdbid = request.POST['imdbid']
        movie.release_year = request.POST['release_year']
        movie.description = request.POST['description']

        movie.save()

        return redirect(moviePageView, movie_id)


def addReviewPageView(request, movie_id):
    data = Movie.objects.get(movie_id=movie_id)

    context = {
        "record": data
    }

    return render(request, 'crudmovies/addreview.html', context)


def addNewReviewPageView(request):
    from datetime import date
    if request.method == 'POST':
        review = Review()

        review.username = request.POST['username']
        review.movie_id = request.POST['movie_id']
        review.rating = request.POST['rating']
        review.description = request.POST['description']
        review.review_date = date.today()

        review.save()

        return redirect(moviePageView, review.movie_id)
