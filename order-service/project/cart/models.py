from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Cart(models.Model):
    user_id = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    quantity = models.IntegerField(
        default=1, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )