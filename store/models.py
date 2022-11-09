from django.db import models
from django.contrib.auth.models import User

# # Create your models here.

class Promotion(models.Model):
    title = models.CharField(max_length=255)

class Collection(models.Model):
    title  = models.CharField(max_length=255)

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)


class Customer(models.Model):
    gold_member = 'G'
    silver_member = 'S'
    bronze_member = 'B'
    membership_status = [
        (gold_member, 'Gold membership'),
        (silver_member, 'Silver membership'),
        (bronze_member, 'Bronze membership'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    memebership = models.CharField(max_length=1, choices=membership_status, default=bronze_member)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Address(models.CharField):
    street_name = models.CharField(max_length=255)
    area = models.CharField(max_length = 255)
    city = models.CharField(max_length=30)
    pincode = models.CharField(max_length=10)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Order(models.Model):
    pending = 'Pending'
    completed = 'Completed'
    failed = 'Failed'
    payment_status = [
        (pending, 'Payment Pending'),
        (completed, 'Payment Confirmed'),
        (failed, 'Payment Failed'),
    ]
    status = models.CharField(max_length=10, choices=payment_status, default=pending)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    

class OrderItem(models.Model):
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    products = models.ForeignKey(Product, on_delete=models.PROTECT)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
