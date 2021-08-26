
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('test/', views.test_api), 
    path('filter-query/<str:text>',views.filter_for_query),
    path('get-user-history/',views.get_history_for_user)
]
