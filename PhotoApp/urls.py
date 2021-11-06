from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('addphoto/', views.addphoto, name='addphoto'),
    path('photo/',views.photo,name='photo'),
    path('allphoto/',views.allphoto,name='allphoto'),

    path('cat/<str:key>/',views.cat,name='cat'),
    path('hat/<str:key>/',views.hat,name='hat'),
    path('dphoto/<int:id>/', views.dphoto, name='dphoto'),


    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),

    path('search',views.search,name='search'),
    path('searching', views.searching, name='searching'),

]