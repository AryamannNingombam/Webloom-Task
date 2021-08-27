
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    # test api
    path('test/', views.test_api), 
    # api for searching for domains
    path('filter-query/<str:text>',views.filter_for_query),
    # api to get the history of searches by the user;
    path('get-user-history/',views.get_history_for_user)
]
