from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class CoffeeShop(models.Model):
    shop_id = models.IntegerField(max_length= 1000)
    shop_name = models.CharField(max_length= 100)
    street = models.CharField(max_length= 100)
    city = models.CharField(max_length= 100)
    state = models.CharField(max_length= 100)
    zipcode = models.IntegerField(max_length= 1000)
    url = models.CharField(max_length= 2000)
    rating = models.IntegerField()
    latitude = models.FloatField()
    longitute = models.FloatField()
    comments = models.CharField(max_length= 1000)

    def __str__(self):
        return f"{self.shop_id}"

class CoffeeShopHours(models.Model):
    shop_id = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE, related_name="shops_hours")
    day_of_week = models.CharField(max_length= 100)
    open_time = models.CharField(max_length= 100)
    close_time = models.CharField(max_length= 100)

class User_CoffeeShop(models.Model):
    shop_id = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE, related_name="visited_shops")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="visitors")
    have_visted = models.BooleanField(default=False)
    will_visit = models.BooleanField(default=False)
    open_time = models.CharField(max_length= 100)
    review_score = models.PositiveIntegerField(max_length= 10)

    def __str__(self):
        return f"{self.user.username} at {self.shop.shop_name}"

