from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def indexPageView():
    return HttpResponse('Index')


def searchPageView(request):
    return HttpResponse('Search')


def listPageView(request):
    return HttpResponse('List')


def indexPageView(request):
    return HttpResponse('Index')

def aboutPageView(Request):
    return HttpResponse('About')

def editMoviePageView(Request):
    return HttpResponse('editMoviePageView')
    
def movieInfoPageView(request, movieID):
    return HttpResponse('MovieInfoPageView')


def addMoviePageView(request):
    return HttpResponse('addMoviePageView')


def addReviewPageView(request):
    return HttpResponse('addReviewPageView')


def addReviewPageView(request, movieID, reviewID):
    return HttpResponse('addReviewPageView')
