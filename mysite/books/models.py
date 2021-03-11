from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Book(models.Model):
    book_title = models.CharField(max_length=100, unique=True)
    book_author = models.CharField(max_length=100)
    book_rating = models.FloatField(
        default=0.0,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    ratings_amount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.book_title}: {self.book_author} - Rating: {self.book_rating} from {self.ratings_amount} rates"
