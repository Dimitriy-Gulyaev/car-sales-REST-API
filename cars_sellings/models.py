from django.db import models


class Car(models.Model):
    year = models.PositiveIntegerField(blank=False, null=False)
    model = models.CharField(max_length=50, blank=False, null=False)
    manufacturer = models.CharField(max_length=50, blank=False, null=False)
    color = models.CharField(max_length=50, blank=True, null=True)
    mileage = models.PositiveIntegerField(default=0)


class Dealer(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)


class Sale(models.Model):
    price = models.PositiveIntegerField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE, blank=False, null=False)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, blank=False, null=False)
