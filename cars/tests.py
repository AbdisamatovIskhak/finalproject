from django.test import TestCase

from .models import Car

class CarModelTestCase(TestCase):
    def setUp(self):
        # Создаем несколько объектов Car для тестирования
        Car.objects.create(model='Model X', brand='Tesla', price_per_day=100.00, available=True)
        Car.objects.create(model='Golf', brand='Volkswagen', price_per_day=50.00, available=False)

    def test_car_str_method(self):
        """Тест метода __str__ модели Car"""
        tesla_model_x = Car.objects.get(model='Model X')
        volkswagen_golf = Car.objects.get(model='Golf')
        self.assertEqual(str(tesla_model_x), 'Tesla Model X')
        self.assertEqual(str(volkswagen_golf), 'Volkswagen Golf')

    def test_car_available_property(self):
        """Тест свойства available модели Car"""
        tesla_model_x = Car.objects.get(model='Model X')
        volkswagen_golf = Car.objects.get(model='Golf')
        self.assertTrue(tesla_model_x.available)
        self.assertFalse(volkswagen_golf.available)

# Create your tests here.
