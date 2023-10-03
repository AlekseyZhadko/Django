from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=300)
    date_registration = models.DateField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField(default=0)
    date_add = models.DateField()
    image = models.ImageField(null=True, blank=True, upload_to='image/')


class Order(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name="order_products")
    sum = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)


