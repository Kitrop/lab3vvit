from django.contrib import admin
from django.urls import path

from django.urls import path

from .views import BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
]