from django.urls import path

from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('add-costs/', views.add_costs, name='add_costs'),
	path('add-profit/', views.add_profit, name='add_profit'),
]
