from django.shortcuts import render
from .api.imdb import searchMovie

# Create your views here.
def addPageView(request):
    if request.method == 'GET':
        return render(request, 'movies/addmovie.html')
    elif request.method == 'POST':
        key = request.POST['title']
        movie = searchMovie(key)
        if movie.title == '':
            context = {
                'msg': 'We could not find your movie, try another one!'
            }
        else:
            context = {
                'msg': 'Is this the movie you\'re looking for?',
                'movie': movie
            }
        return render(request, 'movies/addmovie.html', context)

def deleteMoviePageView(request):
    return render(request, 'movies/addmovie.html')