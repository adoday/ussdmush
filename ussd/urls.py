from  django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *
urlpatterns = [
    path('', views.Murakaza_Neza, name='welcome') ,
    path('ussd/', views.ussdApp, name='ussd')
]
 
