from django.http.response import HttpResponse
from django.urls import path
from .views import indexPageView, aboutPageView, editMoviePageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('', aboutPageView, name='about'),
    path('', editMoviePageView, name='editMovie')
]
