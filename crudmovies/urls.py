from django.urls import path, include
from .views import *

urlpatterns = [
    path('', indexPageView, name='index'),
    path('<str:movieTitle>/<int:movieYear>', moviePageView, name='moviePageView'),
    path('joinus/', joinusPageView, name='joinus'),
    path('about/', aboutPageView, name='about'),
    path('contact/', contactPageView, name='contact'),
    path('search/', searchPageView, name='search'),
    path('list/', listPageView, name='list'),
    path('deleteReview/', deleteReviewView, name='deleteReview'),
    path('editReviewView/', editReviewView, name='editReview'),
    path('addMovie/', addPageView, name='addMovie'),
    path('deleteMovie/<str:movie_title>/<str:movie_year>', deleteMoviePageView, name='deleteMovie'),
]