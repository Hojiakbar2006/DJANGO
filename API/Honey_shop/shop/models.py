from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to="images")
    price = models.IntegerField()
    most_viwed = models.IntegerField(default=0, blank=True)


class Order(models.Model):
     
    class Status(models.TextChoices):
        NOACTIVE = 'OFF'
        ACTIVE = 'ON'

    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=3,
                              choices=Status.choices,
                              default=Status.NOACTIVE)

