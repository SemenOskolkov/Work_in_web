from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import CustomLoginView, UserEditProfileView, CustomEditRegisterView, PasswordEditChangeView, \
    user_activation, PasswordEditResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, \
    simple_reset_password

app_name = UsersConfig.name


class CustomPasswordResetCompleteView:
    pass


urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', CustomEditRegisterView.as_view(), name='register'),
    path('profile/', UserEditProfileView.as_view(), name='profile'),
    path('password/', PasswordEditChangeView.as_view(), name='change_password'),
    path('activate/<str:token>/', user_activation, name='activate'),
    # path('password/reset/', PasswordEditResetView.as_view(), name='password_reset'),  # Сброс пароля (из видео-практики)
    # path('password/reset/<uidb64>/confirm/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password/reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password/reset/complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('simple/reset/', simple_reset_password, name='simple_reset'),

]