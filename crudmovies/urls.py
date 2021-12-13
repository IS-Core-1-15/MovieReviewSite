from django.urls import path, include
from .views import *

urlpatterns = [
    path('', indexPageView, name='index'),
    path('movie/<int:movieID>/', moviePageView, name='moviePageView'),
    path('about/', aboutPageView, name='about'),
    path('search/', searchPageView, name='search'),
    path('list/', listPageView, name='list'),
    path('deleteReview/<int:review_id>', deleteReviewView, name='deleteReview'),
    path('editReviewView/<int:review_id>', editReviewView, name='editReview'),
    path('editExistingReview', editExistingReview, name='editExistingReview'),
    path('addreview/<int:movie_id>', addReviewPageView, name='addReview'),
    path('addNewReview', addNewReviewPageView, name='saveNewReview'),
    path('addMovie/', addPageView, name='addMovie'),
    path('deleteMovie/<str:movie_title>/<str:movie_year>', deleteMoviePageView, name='deleteMovie'),
    path('editMovie/<int:movie_id>', editMoviePageView, name='editMovie'),
    path('editExistingMovie', editExistingMovie, name='editExistingMovie'),
    path('saveMovie/', saveMoviePageView, name='saveMovie')
]
