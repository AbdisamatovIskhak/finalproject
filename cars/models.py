from django.db import models

class Car(models.Model):
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='car_photos', null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model}"

# Create your models here.
