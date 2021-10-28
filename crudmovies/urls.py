from django.urls import path
from .views import deleteMovieView, deleteReviewView, indexPageView, deleteReviewView, editReviewView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('deleteMovie/', deleteMovieView, name='deleteMovie'),
    path('deleteReview/', deleteReviewView, name='deleteReview'),
    path('editReviewView/', editReviewView, name='editReview')
]
