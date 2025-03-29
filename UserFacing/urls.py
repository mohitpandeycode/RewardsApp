from django.urls import path
from .views import index, user_dashboard, userlogout, verify_otp,app_info

urlpatterns = [
    path('', index, name="index"),
    path('user-panel/', user_dashboard, name='user_dashboard'),
    path('user-panel/app-info/<id>', app_info, name='appinfo'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    path('userlogout/', userlogout, name='userlogout'),
]