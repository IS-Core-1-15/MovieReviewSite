from django.urls import path
from .views import indexPageView, movieInfoPageView, addMoviePageView, addReviewPageView, searchPageView, listPageView, aboutPageView, editMoviePageView, deleteMovieView, deleteReviewView, deleteReviewView, editReviewView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('movie/<str:movieID>', movieInfoPageView, name='movieInfoPageView'),
    path('movie/<str:movieID>/editMovie', addMoviePageView, name='addMoviePageView'),
    path('', searchPageView, name='search'),
    path('', listPageView, name='list'),
    path('movie/<str:movieID>/editReview/<int:reviewID>/', addReviewPageView, name='addReviewPageView'),
    path('', aboutPageView, name='about'),
    path('', editMoviePageView, name='editMovie'),
    path('deleteMovie/', deleteMovieView, name='deleteMovie'),
    path('deleteReview/', deleteReviewView, name='deleteReview'),
    path('editReviewView/', editReviewView, name='editReview')
]