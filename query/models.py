from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from authentication.models import CustomUser

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete = models.CASCADE,related_name='user')
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank = True)
    #we can specify upload to proper location
    file_name = models.FileField(upload_to=None, max_length=254)
	

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return "{} posted by {}".format(self.description,self.author)
	
	

	

