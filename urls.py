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
    path('change_user_info', views.ChangeUserInfoView.as_view(), name='change_user_info'),
    path('settings', views.SettingsView.as_view(), name='settings'),
    path('change_user_name/<int:pk>', views.ChangeUserNameView.as_view(), name='change_user_name'),
    path('change_user_email/<int:pk>', views.ChangeUserEmailView.as_view(), name='change_user_email'),
    path('change_user_city/<int:pk>', views.ChangeUserCityView.as_view(), name='change_user_city'),
    path('change_user_phone/<int:pk>', views.ChangeUserPhoneView.as_view(), name='change_user_phone'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('change_password_done/', views.ChangePasswordDoneView.as_view(), name='password_change_done'),
    path('create_ad/', views.AdBoardCreateView.as_view(), name='ad_create'),
    path('ad_created', views.AdBoardCreateDoneView.as_view(), name='ad_created'),
]