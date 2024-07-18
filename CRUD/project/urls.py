from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='homepage'),
    path('delete/<int:id>', views.Delete_record, name="delete"),
    path('<int:id>',views.Update_Record,name='update')
]
