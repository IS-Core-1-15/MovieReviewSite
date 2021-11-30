from django.shortcuts import render

# Create your views here.
def addPageView(request):
    return render(request, 'crudmovies/addmovie.html')

def deleteMoviePageView(request):
    return render(request, 'crudmovies/addmovie.html')