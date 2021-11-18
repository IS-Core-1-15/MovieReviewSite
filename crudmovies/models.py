from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)

    def __str__(self):
        return self.username

class Movie(models.Model):
    title = models.CharField(max_length=30)
    duration = models.IntegerField()
    release_date = models.DateField()
    director = models.CharField(max_length=60)
    main_photo = models.ImageField(upload_to='photos')

    movie_reviews = models.ManyToManyField('User', through='Review')

    def __str__(self):
        return f'{self.title} by {self.director}'
 
class Review(models.Model):
    user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    movie_id = models.ForeignKey(Movie, null=True, blank=True, on_delete=models.SET_NULL)
    rating = models.IntegerField()
    description = models.TextField(max_length=500)
    review_date = models.DateField()

    def __str__(self):
        return f'{self.user_id}: {self.movie_id}-{self.rating}'
