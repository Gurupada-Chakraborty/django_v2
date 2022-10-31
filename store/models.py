from email.policy import default
from itertools import product
from turtle import onclick
from django.db import models

# Create your models here.

class Customer(models.Model):
    member_bronze = 'B'
    member_silver = 'S'
    member_gold = 'G'
    membership_choices = [
        (member_bronze, 'Bronze'),
        (member_silver, 'Silver'),
        (member_gold, 'Gold')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    last_updated = models.DateTimeField(auto_now=True)
    membership = models.CharField(max_length=1, choices=membership_choices, default=member_bronze)

class Address(models.Model):
    street_name = models.CharField(max_length=255)
    area_name = models.CharField(max_length=255)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) # One to many relationship

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    label = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    promotion = models.ManyToManyField(Promotion) # Many to Many relationship
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)


class Order(models.Model):
    payment_success = 'S'
    payment_pending = 'P'
    payment_failed = 'F'
    status = [
        (payment_success, 'Success !'),
        (payment_pending, 'Pending'),
        (payment_failed, 'Failed')
    ]
    payment_status = models.CharField(max_length=1, choices=status, default=payment_pending)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    placed_at = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
