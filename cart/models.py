from django.db import models
from custom_caps.models import Caps
from django.contrib.auth.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    item_caps = models.ForeignKey(Caps, on_delete=models.SET_NULL, null=True, blank=True)
    quantity_caps = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'ID {self.id}: {self.item_caps}'


class DeliveryCost(models.Model):
    STATUS_CHOICES = (
        ('Active', 'active'),
        ('Passive', 'passive')
    )
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default="passive", null=False)
    cost_of_delivery_caps = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    cost_of_caps = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    fixed_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'ID {self.id}: {self.status}: {self.cost_of_caps}'

