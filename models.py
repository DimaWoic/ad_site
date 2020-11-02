from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Country(models.Model):
    name = models.CharField(max_length=250, verbose_name='страна')

    class Meta:
        verbose_name = 'страна'
        verbose_name_plural = 'страны'

    def __str__(self):
        return self.name


class Area(models.Model):
    name = models.CharField(max_length=250, verbose_name='область, край')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='страна', null=True)

    class Meta:
        verbose_name = 'область, край'
        verbose_name_plural = 'области, края'

    def __str__(self):
        return self.name


class City(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name='область, край', null=True)
    name = models.CharField(max_length=250, verbose_name='город, населённый пункт')

    class Meta:
        verbose_name = 'город, населённый пункт'
        verbose_name_plural = 'города, населённые пункты'

    def __str__(self):
        return self.name


class User(AbstractUser):
    phone = PhoneNumberField(verbose_name='номер телефона')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='город, край', null=True)


class Category(models.Model):
    name = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class AddAction(models.Model):
    action = models.CharField(max_length=10, verbose_name='вид объявления')

    class Meta:
        verbose_name = 'вид объявления'
        verbose_name_plural = 'виды объявлений'

    def __str__(self):
        return self.action


class AdBoard(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='город, край', null=True)
    phone = PhoneNumberField(verbose_name='номер телефона')
    description = models.TextField(max_length=500, verbose_name='текст обявления')
    action = models.ForeignKey(AddAction, on_delete=models.CASCADE, verbose_name='вид объявления', null=True)

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'

    def __str__(self):
        return self.title
