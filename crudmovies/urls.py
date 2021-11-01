from django.urls import path
from .views import indexPageView, movieInfoPageView, addMoviePageView, addReviewPageView, searchPageView, listPageView, aboutPageView, editMoviePageView, deleteMovieView, deleteReviewView, deleteReviewView, editReviewView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('movie/<str:movieID>', movieInfoPageView, name='movieInfoPageView'),
    path('addMovie/', addMoviePageView, name='addMoviePageView'),
    path('search/', searchPageView, name='search'),
    path('list/', listPageView, name='list'),
    path('movie/<str:movieID>/addReview/', addReviewPageView, name='addReviewPageView'),
    path('about/', aboutPageView, name='about'),
    path('editMovie/', editMoviePageView, name='editMovie'),
    path('deleteMovie/', deleteMovieView, name='deleteMovie'),
    path('deleteReview/', deleteReviewView, name='deleteReview'),
    path('editReviewView/', editReviewView, name='editReview')
]