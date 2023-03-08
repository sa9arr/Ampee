from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    path('admin/', admin.site.urls),
    path('a/',views.home, name='home'),

    path('a/details/',views.ShowDetails, name='details'),
    path('delete/<int:id>/', views.delete_data, name='deletedata'),
    path('a/<int:id>/', views.update_data, name='updatedata'),


]



 


