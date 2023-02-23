from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordResetForm

from catalog.forms_mixins import StyleFormMixin
from users.models import User


class CustomEditRegisterForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'avatar', 'phone_number', 'country', )


class CustomEditUserForm(StyleFormMixin, UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'avatar', 'phone_number', 'country', )


class PasswordEditResetForm(StyleFormMixin, PasswordResetForm):
    pass
