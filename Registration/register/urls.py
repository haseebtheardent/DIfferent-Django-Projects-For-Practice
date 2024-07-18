from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name="home"),
    path('', views.SignUp, name="signup"),
    path('login/', views.Login, name="login"),
    path('logout/',views.logoutPage, name="logout")
]
