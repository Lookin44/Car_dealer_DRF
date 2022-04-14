from django.db import models


class Dealer(models.Model):
    name = models.CharField(max_length=25, unique=True, db_index=True)
    address = models.TextField()
    car_list = models.ForeignKey(
        'Car',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name


class Car(models.Model):

    class CarBody(models.TextChoices):
        COUPE = 'Coupe'
        SEDAN = 'Sedan'
        HATCHBACK = 'Hatchback'
        CROSSOVER = 'Crossover'

    vin = models.CharField(unique=True, db_index=True, max_length=50)
    brand = models.CharField(max_length=25)
    car_model = models.CharField(max_length=25)
    car_body = models.CharField(max_length=25, choices=CarBody.choices)
    color = models.CharField(max_length=25)
    date_create = models.DateField()
    location = models.ForeignKey('Dealer', on_delete=models.CASCADE)

    def __str__(self):
        return self.vin
