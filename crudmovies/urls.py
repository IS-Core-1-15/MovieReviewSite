from django.urls import path, include
from .views import *

urlpatterns = [
    path('', indexPageView, name='index'),
    path('movie/<int:movieID>/', moviePageView, name='moviePageView'),
    path('joinus/', joinusPageView, name='joinus'),
    path('about/', aboutPageView, name='about'),
    path('contact/', contactPageView, name='contact'),
    path('search/', searchPageView, name='search'),
    path('list/', listPageView, name='list'),
    path('deleteReview/<int:review_id>', deleteReviewView, name='deleteReview'),
    path('editReviewView/', editReviewView, name='editReview'),
    path('addreview/<int:movie_id>', addReviewPageView, name='addReview'),
    path('addNewReview', addNewReviewPageView, name='saveNewReview'),
    path('addMovie/', addPageView, name='addMovie'),
    path('deleteMovie/<str:movie_title>/<str:movie_year>', deleteMoviePageView, name='deleteMovie'),
    path('saveMovie/', saveMoviePageView, name='saveMovie')
]
