from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# from PIL import Image

class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)


    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     image = Image.open(self.Post.path)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})