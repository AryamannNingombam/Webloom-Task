
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('test/', views.test_api, name='test'),
    path('sign-in/', views.sign_in_user, name='sign_in_user'),
    path('sign-up/', views.sign_up_user, name='sign_up_user'),
    path('sign-out/', views.sign_out_user, name='sign_out_user'),
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(),
         name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),



]
