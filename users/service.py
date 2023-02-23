from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail

from users.models import User


def generate_password_and_end_mail(user):
    new_password = User.objects.make_random_password(length=12)
    user.new_password = make_password(new_password)
    user.save()
    send_mail(
        subject='Новый пароль',
        message=f'{new_password}',
        recipient_list=[user.email],
        from_email=settings.EMAIL_HOST_USER
    )