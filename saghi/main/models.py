from django.db import models

# Create your models here.
class section(models.Model):
    title = models.CharField(max_length=250)
    Description = models.TextField(null=True,blank=True)
    poster = models.ImageField(upload_to='media/img',null=True,blank=True)
    page_movies = models.URLField(null=True,blank=True)
    
    
    def __str__(self):
        return f"{self.title} | {self.Description[:50]}"