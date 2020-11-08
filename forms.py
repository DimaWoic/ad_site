from django import forms
from .models import User
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
import phonenumbers


class RegForm(forms.ModelForm):
    username = forms.CharField(max_length=50, label='Логин')
    first_name = forms.CharField(max_length=250, label='Имя')
    last_name = forms.CharField(max_length=250, label='Фамилия')
    phone = forms.CharField(label='Номер телефона')
    password1 = forms.CharField(label='пароль', widget=forms.PasswordInput, min_length=8)
    password2 = forms.CharField(label='пароль, ещё один раз', widget=forms.PasswordInput,
                                help_text='Введите пароль ещё раз', min_length=8)

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            errors = {'password2': ValidationError('Пароли не совпадют', code='password_mismatch')}
            raise ValidationError(errors)
        if password2 != password1:
            errors = {'password1': ValidationError('Пароли не совпадют', code='password_mismatch')}
            raise ValidationError(errors)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('Пользователь с таким логином уже существует', code='invalid')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Пользователь с такой электронной почтой уже существует', code='invalid')
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        phone_validation = phonenumbers.parse(phone, None)
        if User.objects.filter(phone=phone).exists():
            raise ValidationError('Данный номер уже зарегистрирован', code='invalid')
        if not phonenumbers.is_possible_number(phone_validation):
            raise ValidationError('Введите номер телефона в формате +79123456789')
        return phone

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        user.is_activated = True
        user.is_superuser = False
        if commit:
            user.save()

    class Meta:
        model = User
        fields = ['city', 'username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2']


class ChangeUserName(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ChangeUserEmailForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Пользователь с такой электронной почтой уже существует', code='invalid')
        return email


class ChangeUserCityForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['city']


class ChangeUserPhoneForm(forms.ModelForm):
    phone = forms.CharField(label='Номер телефона')

    class Meta:
        model = User
        fields = ['phone']

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        phone_validation = phonenumbers.parse(phone, 'RU')
        if User.objects.filter(phone=phone).exists():
            raise ValidationError('Данный номер уже зарегистрирован', code='invalid')
        if not phonenumbers.is_possible_number(phone_validation):
            raise ValidationError('Введите номер телефона в формате +79123456789')
        return phone
