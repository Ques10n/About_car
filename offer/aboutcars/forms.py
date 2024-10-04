from django import forms
from django.contrib.auth import get_user_model, get_user
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Comment, Car


class CommentForm(forms.ModelForm):
    content = forms.CharField(label= 'Напишите комментарий', widget= forms.Textarea())
    author = forms.CharField(widget= forms.HiddenInput(), required=False)
    car = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Comment
        fields = ['content']


class AddCar(forms.ModelForm):
    make = forms.CharField(max_length= 255, label= 'Марка')
    model = forms.CharField(max_length= 255, label= 'Модель')
    year = forms.IntegerField(label= 'Год выпуска')
    description = forms.CharField(widget= forms.Textarea(), label= 'Описание')
    owner = forms.CharField(widget= forms.HiddenInput(), required=False)

    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'description']



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label= 'Логин', max_length= 255)
    password1 = forms.CharField(label= 'Пароль', widget= forms.PasswordInput())
    password2 = forms.CharField(label= 'Повторите пароль', widget= forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {'email': 'E-mail',
                  'first_name': 'Имя',
                  'last_name': 'Фамилия', }


    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email= email).exists():
            raise forms.ValidationError('Такой email уже существует')
        return email


    def clean_username(self):
        username = self.cleaned_data['username']
        if get_user_model().objects.filter(username= username).exists():
            raise forms.ValidationError('Такой логин уже существует')
        return username


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label= 'Логин', widget= forms.TextInput(attrs={'class':'form_input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form_input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class UpdateCarForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(), label='Описание')
    author = forms.CharField(widget=forms.HiddenInput(), required=False)
    car = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Car
        fields = ['description']


class ConfirmDeleteForm(forms.Form):
    pass



