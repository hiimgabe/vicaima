# pylint: disable=all
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('add_event/', views.add_event, name="add_event"),
	path('add_user/', views.add_user, name="add_user"),
	path('aval_form', views.aval_form, name="aval_form"),
	path('aval_list', views.aval_list, name="aval_list"),
	path('show_events/', views.show_events, name='show_events'),
	path('change_status/<int:event_id>/', views.change_status, name='change_status'),

]