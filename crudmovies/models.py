from django.db import models

# Create your models here.
class Person(models.Model):
    person_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30)

    class Meta:
        db_table = 'person'

    def __str__(self):
        return self.username


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    imdbid = models.CharField(max_length=10)
    runtime = models.CharField(max_length=10)
    release_year = models.IntegerField()
    description = models.TextField(max_length=300)
    main_photo = models.URLField(max_length=200)
    imdb_rating = models.FloatField()

    movie_reviews = models.ManyToManyField('Person', through='Review')

    class Meta:
        db_table = 'movie'

    def __str__(self):
        return f'{self.title} by {self.release_year}'
 

class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    person = models.ForeignKey(
        'Person',
        on_delete=models.CASCADE,
        to_field='person_id',
        db_column='person_id'
    )
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
        return f'{self.person}: {self.movie}-{self.rating}'
