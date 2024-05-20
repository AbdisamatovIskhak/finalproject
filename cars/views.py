from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Car
from django.shortcuts import render, redirect
from .forms import CarForm

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'cars/add_car.html', {'form': form})

def car_list(request):
    cars = Car.objects.filter(available=True)
    return render(request, 'cars/car_list.html', {'cars': cars})



def car_detail(request, car_id):
    car = Car.objects.get(pk=car_id)
    return render(request, 'cars/car_detail.html', {'car': car})

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def order_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return HttpResponse(f'Вы заказали автомобиль: {car.model}')



# Create your views here.
