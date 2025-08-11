# from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    
    # path('admin/', admin.site.urls),
    path('',views.register,name='register'),
    path('login',views.user_login,name='login'),
    path('home',views.home,name='home'),
    path('logout',views.user_logout,name='logout'),
    path('profile',views.profile,name='profile'),
    path('update',views.update,name='update'),
    path('forget_password',views.forget_password,name='forget_password')
    


]