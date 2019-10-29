from django.db import models

class Subscriber(models.Model):
    """
        Subscriber to blog's posts
    """
    email = models.EmailField(
        max_length=200, null=False, unique=True
    )

    def __str__(self):
        return str(self.email)