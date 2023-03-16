from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('admin/', admin.site.urls),
    path('',views.signin, name='signin'),
    path('signin/',views.signin, name='signin'),
    path('signup/',views.signup, name='signup'),
    path('home/',views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(next_page='signin'), name='logout'),

    path('details/',views.ShowDetails, name='details'),
    path('delete/<int:id>/', views.delete_data, name='deletedata'),
    path('<int:id>/', views.update_data, name='updatedata'),


]



 


