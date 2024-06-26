from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='main_page'),
    path('Profile', views.Profile, name='profile'),
    path('Registration.html', views.register_to_account, name='registration'),
    path('Login.html', views.login_to_account, name='login'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('Logout', views.Logout, name='Logout'),
]