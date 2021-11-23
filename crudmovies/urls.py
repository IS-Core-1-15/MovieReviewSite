from django.urls import path
from .views import *

urlpatterns = [
    path('', indexPageView, name='index'),
    path('movie/<str:movieTitle>/<str:director>', moviePageView, name='moviePageView'),
    path('joinus/', joinusPageView, name='joinus'),
    path('about/', aboutPageView, name='about'),
    path('contact/', contactPageView, name='contact'),
    path('addMovie/', addMoviePageView, name='addMoviePageView'),
    path('search/', searchPageView, name='search'),
    path('list/', listPageView, name='list'),
    path('movie/<str:movieID>/addReview/', addReviewPageView, name='addReviewPageView'),
    path('editMovie/', editMoviePageView, name='editMovie'),
    path('deleteMovie/', deleteMovieView, name='deleteMovie'),
    path('deleteReview/', deleteReviewView, name='deleteReview'),
    path('editReviewView/', editReviewView, name='editReview')
]