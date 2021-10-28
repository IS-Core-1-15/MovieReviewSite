from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def indexPageView():
    return HttpResponse('Index')


def searchPageView(request):
    return HttpResponse('Search')


def listPageView(request):
    return HttpResponse('List')
