from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ["first_name", "last_name", "email_address"]
        unique_together = ("first_name", "last_name", "email_address")

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    content = models.TextField(MinValueValidator(10))
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True ,related_name="posts")
    slug = models.SlugField(unique=True, default="",blank=True, null=False, db_index=True)
    image_name = models.CharField(max_length=100, null=True)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["title", "author", "slug"]
        unique_together = ("title", "author", "slug")


