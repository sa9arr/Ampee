from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    path('admin/', admin.site.urls),
    path('a/',views.ShowDetails),
    path('delete/<int:id>/', views.delete_data, name='deletedata'),
    path('<int:id>/', views.update_data, name='updatedata'),


]



 


