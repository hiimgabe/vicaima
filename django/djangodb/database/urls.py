from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('add_event/', views.add_event, name="add_event"),
	path('add_user/', views.add_user, name="add_user"),
]