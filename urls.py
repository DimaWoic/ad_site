from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('register', views.RegistrationView.as_view(), name='registration'),
    path('registration_done', views.RegisterDoneView.as_view(), name='reg_done'),
    path('login', views.BoardLogin.as_view(), name='login'),
    path('account', views.UserLK.as_view(), name='lk'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('logout_done', views.LogOutDone.as_view(), name='logout_done'),
]