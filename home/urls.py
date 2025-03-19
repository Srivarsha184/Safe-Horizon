from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.main,name='main'),
    path("adminlogin",views.adminlogin,name='adminlogin'),
   path("admindashboard",views.admindashboard,name='admindashboard'),
    path("login/", views.user_login, name='user_login'),
    path("signup", views.signup, name='signup'),
    path("dashboard/",views.dashboard,name='dashboard'),
    path("profile",views.profile,name='profile'),
    path("yourreports",views.yourreports,name='yourreports'),
    path("report",views.report,name='report'),
    path("logout",views.logout,name='logout'),
    path("adminreports",views.adminreports,name='adminreports'),
    path('delete_user', views.delete_user, name='delete_user')
    # path('pie_chart/', views.pie_chart_view, name='pie_chart')

]