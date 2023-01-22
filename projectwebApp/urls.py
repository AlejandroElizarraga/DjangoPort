from django.urls import path
from projectwebApp import views
urlpatterns = [
    path('', views.home),
    path('sent_mail/', views.contacto),
]
