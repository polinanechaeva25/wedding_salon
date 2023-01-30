from django.contrib import admin
from django.urls import path, include
from mainapp.views import MainListView, EmailView

app_name = 'mainapp'

urlpatterns = [
    path('', MainListView.as_view(), name='index'),
    path('email/', EmailView.as_view(), name='send_email'),
]
