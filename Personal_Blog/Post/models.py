import django
from django.db import models


class Post(models.Model):
    """
        Post inside my blog
    """
    title = models.CharField(max_length=200, null=False)
    paragraph = models.TextField(null=False)
    date = models.DateTimeField(default=django.utils.timezone.now, null=False)
    image = models.ImageField(upload_to='posts', null=True)

    def __str__(self):
        return str(self.id) + " " + self.title
