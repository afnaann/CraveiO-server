from django.db import models


class Order(models.Model):
    STATUS_CHOICES = [
        ("SH", "Shipping"),
        ("OR", "Order Received"),
        ("CA", "Cancelled"),
        ("RT", "Returned"),
        ("RF", "Refunded"),
    ]

    user_id = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    address = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="SH")


class OrderItems(models.Model):
    order = models.ForeignKey(
        Order, related_name="order_set", on_delete=models.CASCADE
    )
    product_id = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)

