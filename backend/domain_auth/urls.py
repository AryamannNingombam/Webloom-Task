
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # test api for checking if the url is working;
    path('test/', views.test_api, name='test'),
    # api to sign up, token free;
    path('sign-up/', views.sign_up_user, name='sign_up_user'),
    # api to sign out, not used as of now, karle bc
    path('sign-out/', views.sign_out_user, name='sign_out_user'),
    # api to check if the user is verified using the username,
    # id can also be used.
    path('check-user-verified/<str:username>',views.check_user_verified,name="check_user_verified"),

    # getting jwt token;
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(),
         name='token_create'),  # override sjwt stock token

    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # getting information on the logged in user;
    path('get-user-information/',views.get_user_information,name="get-user-information"),
    # verifying the email of a user;
    path('verify-mail/<str:hash>',views.verify_mail,name="verify-email")



]
