from django.conf import settings
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from cars.models import Car


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    # orders/models.py


    def __str__(self):
        return f'Order {self.id} by {self.user.username} for {self.car.model}'

    # Добавьте любые другие поля, которые вам нужны для заказа, например, количество дней аренды и т.д.

    

    
# Create your models here.
