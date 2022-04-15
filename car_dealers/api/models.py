from django.db import models


class Dealer(models.Model):
    name = models.CharField(
        max_length=25,
        unique=True,
        db_index=True,
        blank=False
    )
    address = models.TextField()

    def __str__(self):
        return self.name


class Car(models.Model):

    class CarBody(models.TextChoices):
        COUPE = 'Coupe'
        SEDAN = 'Sedan'

    vin = models.CharField(
        unique=True,
        db_index=True,
        max_length=50,
        blank=False
    )
    brand = models.CharField(max_length=25, blank=False)
    car_body = models.CharField(max_length=25, choices=CarBody.choices)
    date_create = models.DateField(auto_now_add=True, blank=False)
    location = models.ForeignKey(
        'Dealer',
        on_delete=models.CASCADE,
        related_name='cars'
    )

    def __str__(self):
        return self.vin
