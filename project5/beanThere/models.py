from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    text = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="op")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"post{self.id} posted by {self.user} on {self.date.strftime('%d %b %Y at %H:%M:%S')}"