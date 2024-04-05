from django.db import models

# Create your models here.
fuel=[
    ('Diesel','Diesel'),
    ('Petrol','Petrol'),
    ('CNG','CNG'),
]

class FuelTypeModel(models.Model):
    Fuel_name=models.CharField(max_length=300, choices=fuel)
    def __str__(self):
        return self.Fuel_name
    
Car=[
        ('Tata','Tata'),
        ('Audi','Audi'),
        ('Toyata','Toyata'),
        ('Honda','Honda')
    ]

class CarModel(models.Model):
    Car_name=models.CharField(max_length=300, choices=Car)
    Car_fuel=models.ManyToManyField(FuelTypeModel)
    def __str__(self):
        return self.Car_name