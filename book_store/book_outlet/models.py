from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        ordering = ["name"]


class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street} {self.postal_code} {self.city}"
    
    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Address Entries"
        ordering = ["street", "postal_code", "city"]
        unique_together = ("street", "postal_code", "city")


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return self.full_name()
    
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ["first_name", "last_name"]

class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="",blank=True, null=False, db_index=True)
    published_countries = models.ManyToManyField(Country, blank=True)

    def __str__(self):
        return f"{self.title} ({self.rating})"

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ["title", "rating", "author", "is_bestselling"]
