from django.urls import path, include
from .views import *

urlpatterns = [
    path('addMovie/', addPageView, name='addMovie'),
    path('deleteMovie/', deleteMoviePageView, name='deleteMovie'),
]