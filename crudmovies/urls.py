from django.urls import path
from .views import indexPageView

urlpatterns = [
    path('', indexPageView, name='index'),
]




















































deleteMovieView, deleteReviewView, deleteReviewView, editReviewView

path('deleteMovie/', deleteMovieView, name='deleteMovie'),
path('deleteReview/', deleteReviewView, name='deleteReview'),
path('editReviewView/', editReviewView, name='editReview')