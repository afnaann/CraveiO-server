from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Restaurant(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=40)
    license_image = models.ImageField(upload_to='shop_licenses/', help_text="Upload the shop's license image")
    latitude = models.DecimalField(
        max_digits=9,  
        decimal_places=6, 
        validators=[
            MinValueValidator(8.18),
            MaxValueValidator(12.48)
        ],
        help_text="Sorry, Restaurants Are Only From Kerala"
    )
    longitude = models.DecimalField(
        max_digits=9,  
        decimal_places=6, 
        validators=[
            MinValueValidator(74.70),
            MaxValueValidator(77.30)
        ],
        help_text="Sorry, Restaurants Are Only From Kerala"
    )
    open_time = models.TimeField()
    close_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    dish_image = models.ImageField(upload_to='dishes/',help_text="Upload the Dish image")
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    