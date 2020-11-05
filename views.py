from django.shortcuts import render
from .models import AdBoard, User
from .forms import RegForm, ChangeUserInfo
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
    form_class = RegForm
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


class ChangeUserInfoView(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = User
    form_class = ChangeUserInfo
    success_message = 'Личные данные изменены'
    success_url = reverse_lazy('lk')
    template_name = 'board/change_info.html'

