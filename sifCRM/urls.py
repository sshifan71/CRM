"""
URL configuration for sifCRM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from leads import views
from django.contrib.auth.views import( 
    LoginView, 
    LogoutView, 
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordContextMixin
    
)
urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing_page'),
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls')),
    path('agents/', include('agents.urls')),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('reset_pass/', PasswordResetView.as_view(), name = 'reset_pass'),
    path('pass_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('pass_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='pass_reset_confirm'),
    path('pass _reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),


]
