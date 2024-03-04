from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),
     path('', views.login, name='login'),
     path('logout/', views.logout, name='logout'),
    path('Patient/', views.Patient1, name='Patient1'),
    path('Doctor/', views.Doctor1, name='Doctor1'),

   
    # Add URL patterns for login and dashboards
]
