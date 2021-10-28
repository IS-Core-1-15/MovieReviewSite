from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request):
    return HttpResponse('Index')








































def editReviewView(request) :
    return HttpResponse('Edit Review')

def deleteMovieView(request) :
    return HttpResponse('Delete Movie')

def deleteReviewView(request) :
    return HttpResponse('Delete Review')