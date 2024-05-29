from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='main_page'),
    path('registration.html', views.register_to_account, name='registration'),
    path('login.html', views.login_to_account, name='login'),
]