from django.contrib import admin
from .models import AdBoard, AddAction, AbstractUser, Area, City, Country, Category, User

# Register your models here.


class AdboardAdmin(admin.ModelAdmin):
    model = AdBoard
    list_display = ['city', 'category', 'action', 'phone', 'title', 'description', 'image']


class AddActionAdmin(admin.ModelAdmin):
    model = AddAction
    list_display = ['action']


class AreaAdmin(admin.ModelAdmin):
    model = Area


class CityAdmin(admin.ModelAdmin):
    model = City


class CountryAdmin(admin.ModelAdmin):
    model = Country


class CategoryAdmin(admin.ModelAdmin):
    model = Category


class UserAdmin(admin.ModelAdmin):
    model = User


admin.site.register(User, UserAdmin)
admin.site.register(AdBoard, AdboardAdmin)
admin.site.register(AddAction, AddActionAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Category, CategoryAdmin)
