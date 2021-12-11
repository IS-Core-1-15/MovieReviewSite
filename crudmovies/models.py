from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    imdbid = models.CharField(max_length=10)
    runtime = models.CharField(max_length=10)
    release_year = models.IntegerField()
    description = models.TextField(max_length=300)
    main_photo = models.URLField(max_length=200)
    imdb_rating = models.FloatField()

    class Meta:
        db_table = 'movie'

    @classmethod
    def create(self, movie):
        movie = self(
            title = movie.title,
            imdbid = movie.imdbid,
            runtime = movie.runtime,
            release_year = movie.year,
            description = movie.description,
            main_photo = movie.main_photo,
            imdb_rating = movie.imdb_rating,
        )
        return movie

    def __str__(self):
        return f'{self.title} by {self.release_year}'
 

class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30)
    movie = models.ForeignKey(
        'Movie',
        on_delete=models.CASCADE,
        to_field='movie_id',
        db_column='movie_id'
    )
    rating = models.IntegerField()
    description = models.TextField(max_length=500)
    review_date = models.DateField()

    class Meta:
        db_table = 'review'

    def __str__(self):
        return f'{self.username}: {self.movie}-{self.rating}'
