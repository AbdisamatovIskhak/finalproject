
from django.shortcuts import render, redirect
from .forms import OrderForm
from cars.models import Car
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Car, Order

@login_required
def create_order(request, car_id):
    car = Car.objects.get(pk=car_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.car = car
            order.save()
            car.available = False
            car.save()
            return redirect('car_list')
    else:
        form = OrderForm()
    return render(request, 'orders/create_order.html', {'form': form})

def order_detail(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def order_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    Order.objects.create(user=request.user, car=car)
    return HttpResponse(f'Вы заказали автомобиль: {car.model}')
# orders/views.py


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def order_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.car = car
            order.save()
            return HttpResponse(f'Вы заказали автомобиль: {car.model}')
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form, 'car': car})


# Create your views here.
