from django.conf import settings
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView, \
    PasswordResetDoneView, PasswordResetCompleteView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, CreateView

from users.forms import CustomEditUserForm, CustomEditRegisterForm, PasswordEditResetForm
from users.models import User
from users.service import generate_password_and_end_mail


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class CustomEditRegisterView(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = CustomEditRegisterForm
    success_url = '/'


    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.object.is_active = False
            self.object.token = User.objects.make_random_password(length=15)
            send_mail(
                subject='Активация',
                message=f' http://127.0.0.1:8000/users/activate/{self.object.token}/',

                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[self.object.email],
                fail_silently=False,

            )
            self.object.is_active = True
            self.object.save()
        return super().form_valid(form)


class UserEditProfileView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = CustomEditUserForm

    def get_object(self, queryset=None):
        return self.request.user


class PasswordEditChangeView(PasswordChangeView):
    success_url = '/'
    template_name = 'users/change_password.html'


class PasswordEditResetView(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    form_class = PasswordEditResetForm
    success_url = reverse_lazy('users:password_reset_done')
    email_template_name = 'users/email_reset.html'
    from_email = settings.EMAIL_HOST_USER


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/reset_done.html'


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/reset_complete.html'


def simple_reset_password(request):
    if request.method == 'POST':
        current_user = User.objects.filter(email=request.POST.get('email')).first()
        if current_user:
            generate_password_and_end_mail(current_user)
    return render(request, 'users/simple_reset.html')


def confirm_new_generated_password(request):
    current_user = User.objects.filter(email=request.GET.get('email')).first()
    current_user.password = current_user.new_password
    current_user.new_password = None
    current_user.save()


def user_activation(request, token):
    u = User.objects.filter(token=token)

    return redirect(reverse('catalog:home'))