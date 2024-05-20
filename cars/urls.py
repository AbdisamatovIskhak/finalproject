from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add/', views.add_car, name='add_car'),
    path('', views.car_list, name='car_list'),
    path('<int:car_id>/', views.car_detail, name='car_detail'),
    path('order/<int:car_id>/', views.order_car, name='order_car')  
    # path('<int:car_id>/update/', views.update_car, name='update_car'),  # URL для обновления информации об автомобиле
    # path('<int:car_id>/delete/', views.delete_car, name='delete_car'),  # URL для удаления автомобиля
]

static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

