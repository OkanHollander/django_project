from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Review(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.CharField(max_length=250)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.user_name
    
    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ["user_name"]

