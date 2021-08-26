
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('test/', views.test_api, name='test'),
    path('sign-up/', views.sign_up_user, name='sign_up_user'),
    path('sign-out/', views.sign_out_user, name='sign_out_user'),
    path('check-user-verified/<str:username>',views.check_user_verified,name="check_user_verified"),
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(),
         name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('get-user-information/',views.get_user_information,name="get-user-information"),
    path('verify-mail/<str:hash>',views.verify_mail,name="verify-email")



]
