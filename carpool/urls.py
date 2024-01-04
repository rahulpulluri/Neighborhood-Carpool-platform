from django.urls import path

from . import views

app_name = "carpool"
urlpatterns = [
    path('', views.login, name='login'),
    path('carpool/', views.pages_home, name='pages_home'),
    path('ride/', views.ride, name='ride'),
    path('createCarpool/', views.createCarpool, name='createCarpool'),
    path('myCarpool/', views.myCarpool, name='myCarpool'),
    path('ride/success/', views.success, name='success'),
    path('carpool/<str:carpool_id>/', views.carpool_detail, name='carpool_detail'),
    path('carpool/increment', views.carpool_increment, name='carpool-increment'),
    path('carpool/decrement', views.carpool_decrement, name='carpool-decrement'),
    path('carpool/edit/<int:carpool_id>/', views.edit_carpool, name='edit_carpool'),
    path('carpool/delete/<int:carpool_id>/', views.delete_carpool, name='delete_carpool'),

]
