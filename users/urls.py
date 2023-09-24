from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import dashboard, register, edit, LoginView
from django.contrib.auth import views as auth_views
# from login_app.views import user_login_old

urlpatterns = [
    # all path
    # path('', include('django.contrib.auth.urls')),

    # dashboard
    path('', dashboard, name='dashboard'),

    #  register
    path('register/', register, name='register'),

    # edit profile
    path('edit/', edit, name='edit'),

    # previous login view
    # path('login/', user_login_old, name='login'),

    # login
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # password-change
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # password-reset
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

