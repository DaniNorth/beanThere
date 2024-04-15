from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')


class CoffeeShop(models.Model):
    shop_id = models.CharField(primary_key=True)  # Assuming shop_id is unique
    shop_name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    url = models.CharField(max_length=200)
    rating = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    comments = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.shop_name}"


class CoffeeShopHours(models.Model):
    shop = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE, related_name="hours")
    day_of_week = models.CharField(max_length=20)
    open_time = models.CharField(max_length=20)
    close_time = models.CharField(max_length=20)


class Rating(models.Model):
    shop = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    score = models.PositiveIntegerField()

    class Meta:
        unique_together = ('shop', 'user')


class Comment(models.Model):
    shop = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class UserCoffeeShop(models.Model):
    shop = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    have_visited = models.BooleanField(default=False)
    will_visit = models.BooleanField(default=False)

    class Meta:
        unique_together = ('shop', 'user')
