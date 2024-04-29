from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    class Meta:
        verbose_name_plural = "Author Entries"
class Tag(models.Model):
    caption = models.CharField(max_length=50)
class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author,null=True,on_delete=models.SET_NULL,related_name="posts")
    tag = models.ManyToManyField(Tag)


   
