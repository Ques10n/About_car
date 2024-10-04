from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from aboutcars.forms import CommentForm, RegisterUserForm, LoginUserForm, AddCar, UpdateCarForm
from aboutcars.models import Car, Comment


def car_list(request):
    cars = Car.objects.all()
    context = {
        'cars': cars
    }
    return render(request, template_name= 'aboutcars/car_list.html', context= context)


def car_detail(request, car_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.car_id = car_id
            comment.save()
            return redirect('car_detail', car_id=car_id)
    else:
        form = CommentForm(initial= {'author': request.user.id})

    car = get_object_or_404(Car, id=car_id)
    comments = Comment.objects.filter(car_id= car_id)
    return render(request, 'aboutcars/about_cars.html', {
        'car': car,
        'comments': comments,
        'form': form,
    })


def add_car(request):
    if request.method == 'POST':
        form = AddCar(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            form.save()
            return redirect('car_list')
    else:
        form = AddCar()

    data = {
        'form': form
    }
    return render(request, template_name= 'aboutcars/add_car.html', context= data)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'aboutcars/login.html'
    extra_context = {'title': 'Авторизация'}


    def get_success_url(self):
        return reverse_lazy('car_list')


def logout_user(request):
    logout(request)
    return render(request, 'aboutcars/car_list.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'aboutcars/register.html'
    success_url = reverse_lazy('login')


def update_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        print(request.POST)
        if 'delete' in request.POST:
            car.delete()
            return redirect('car_list')
        else:
            form = UpdateCarForm(request.POST, instance=car)
            if form.is_valid():
                car = form.save(commit=False)
                car.owner = request.user
                car.car_id = car_id
                car.save()
                return redirect('car_detail', car_id=car_id)


    form = UpdateCarForm(initial={'owner': request.user.id})
    return render(request, 'aboutcars/car_update.html', {
        'form': form,
        'car': car,
    })
