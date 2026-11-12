from django.contrib import admin
from django.urls import path
from nitsapp import views

urlpatterns = [path('', views.calcs_churn, name='calcs_churn'),]