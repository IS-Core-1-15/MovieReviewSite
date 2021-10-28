from django.urls import path
from .views import indexPageView, movieInfoPageView, addMoviePageView, addReviewPageView, searchPageView, listPageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('movie/<str:movieID>', movieInfoPageView, name='movieInfoPageView'),
    path('movie/<str:movieID>/editMovie',
         addMoviePageView, name='addMoviePageView'),
    path('movie/<str:movieID>/editReview/<int:reviewID>/',
         addReviewPageView, name='addReviewPageView'),
    path('', searchPageView, name='search'),
    path('', listPageView, name='list'),
    path('movie/addMovie', addMoviePageView, name='addMoviePageView'),
    path('movie/<str:movieID>/editReview/<int:reviewID>/',
         addReviewPageView, name='addReviewPageView'),
]
