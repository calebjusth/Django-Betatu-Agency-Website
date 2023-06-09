from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginpage, name="login"),
    path('sign_up/', views.signup, name="sign_up"),
    path('blog/', views.post, name="blog"),
    path('logout/', views.logoutuser, name="logout"),
    path('procceed/', views.proceed_page, name="procceed"),
    path('profiles/', views.profiles, name="profiles"),
    path('profile_setup/', views.profile_setup, name="profile_setup"),



    #password set_up
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password" ),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_done.html"), name="password_reset_complete"),
]