from django.db import models
from django.contrib.auth.models import User

# # Create your models here.

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField(null=True)

class Collection(models.Model):
    title  = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    slug = models.SlugField(null=True)
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
    birth_date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    membership = models.CharField(max_length=1, choices=membership_status, default=bronze_member)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Address(models.CharField):
    street_name = models.CharField(max_length=255)
    area = models.CharField(max_length = 255)
    city = models.CharField(max_length=30)
    pincode = models.CharField(max_length=10)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

class Order(models.Model):
    pending = 'Pending'
    completed = 'Completed'
    failed = 'Failed'
    status = [
        (pending, 'Payment Pending'),
        (completed, 'Payment Confirmed'),
        (failed, 'Payment Failed'),
    ]
    payment_status = models.CharField(max_length=10, choices=status, default=pending)
    placed_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    

class OrderItem(models.Model):
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
