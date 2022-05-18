from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('home', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
]