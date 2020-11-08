from django.shortcuts import render
from .models import AdBoard, User
from . import forms
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    adds = AdBoard.objects.all()
    context = {'adds': adds}
    return render(request, template_name='board/index_adds.html', context=context)


class RegistrationView(CreateView):
    form_class = forms.RegForm
    template_name = 'board/registration.html'

    def get_success_url(self, **kwargs):
        if kwargs == None:
            return reverse_lazy('reg_done')
        return reverse_lazy('reg_done')


class RegisterDoneView(TemplateView):
    template_name = 'board/register_done.html'


class BoardLogin(LoginView):
    template_name = 'board/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = reverse_lazy('lk')
        return context


class UserLogoutView(LogoutView, LoginRequiredMixin):
    next_page = 'logout_done'
    template_name = 'board/logout.html'


class LogOutDone(TemplateView):
    template_name = 'board/logout.html'


class UserLK(TemplateView, LoginRequiredMixin):
    template_name = 'board/lk.html'


class ChangeUserInfoView(LoginRequiredMixin, TemplateView):
    template_name = 'board/change_info.html'


class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'board/settings.html'


class ChangeUserNameView(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = User
    form_class = forms.ChangeUserName
    success_message = 'Имя и фамилия изменены'
    success_url = reverse_lazy('change_user_info')
    template_name = 'board/change_name.html'


class ChangeUserEmailView(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = User
    form_class = forms.ChangeUserEmailForm
    success_message = 'Электронная почта изменена'
    success_url = reverse_lazy('change_user_info')
    template_name = 'board/change_email.html'


class ChangeUserCityView(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = User
    form_class = forms.ChangeUserCityForm
    success_message = 'Ваш город изменён'
    success_url = reverse_lazy('change_user_info')
    template_name = 'board/change_city.html'


class ChangeUserPhoneView(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = User
    form_class = forms.ChangeUserPhoneForm
    success_message = 'Номер телефона изменён'
    success_url = reverse_lazy('change_user_info')
    template_name = 'board/change_phone.html'


class ChangePasswordView(PasswordChangeView, LoginRequiredMixin):
    template_name = 'board/change_password.html'
    success_url = reverse_lazy('pass_change_done')


class ChangePasswordDoneView(PasswordChangeDoneView, LoginRequiredMixin):
    template_name = 'board/password_change_done.html'
