from django.urls import path
from .views import admin_dashboard, add_app, home,adminlogout,update_app,deleteApp,userInfo,app_not_valid


urlpatterns = [
    path('', home, name="home"),
    path('admin-panel/', admin_dashboard, name='admin_dashboard'),
    path('admin-panel/add-app/', add_app, name='add_app'),
    path('admin-panel/update-app/<id>', update_app, name='update_app'),
    path('admin-panel/delete-app/<id>', deleteApp, name='deleteApp'),
    path('admin-panel/user-info/<id>', userInfo, name='userinfo'),
    path('admin-panel/image-notvalid/<int:app_id>/',app_not_valid, name='notvalid'),
    path('adminlogout/',adminlogout,name='adminlogout'),
]