from django.urls import path

from . import views


urlpatterns = [
	path('', views.index, name='index')
]

# ,
# 	path('finance/<int:poll_id>', views.poll, name='poll'),
# 	path('results/', views.results, name='results'),
# 	path('create_user/', views.create_user, name='create_user'),
# 	path('authenticate/', views.authenticate, name='authenticate'),
# 	path('logout/', views.logout, name='logout')