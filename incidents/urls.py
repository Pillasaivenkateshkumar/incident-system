from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_incident, name='create'),
    path('update/<int:incident_id>/', views.update_incident, name='update'),
    path('delete/<int:incident_id>/', views.delete_incident, name='delete'),
]