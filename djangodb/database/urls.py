# pylint: disable=all
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('add_event/', views.add_event, name="add_event"),
	path('add_user/', views.add_user, name="add_user"),
	path('add_user_csv/', views.add_user_csv, name="add_user_csv"),
	path('eval_form', views.eval_form, name="eval_form"),
	path('evaluated_form', views.evaluated_form, name="evaluated_form"),
	path('eval_list', views.eval_list, name="eval_list"),
	path('show_events/', views.show_events, name='show_events'),
	path('change_status/<int:event_id>/', views.change_status, name='change_status'),

]