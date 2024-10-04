from django.contrib.auth.views import LogoutView
from django.urls import path

from aboutcars.views import car_list, car_detail, LoginUser, logout_user, add_car, update_car, RegisterUser

urlpatterns = [
    path('', car_list, name='car_list'),
    path('<int:car_id>/', car_detail, name='car_detail'),
    path('add_car', add_car, name= 'add_car'),
    path('login', LoginUser.as_view(), name= 'login'),
    path('logout', LogoutView.as_view(next_page= 'car_list'), name = 'logout'),
    path('register', RegisterUser.as_view(), name= 'register'),
    path('<int:car_id>/update/', update_car, name= 'update'),
]
