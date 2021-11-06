from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [
       url('^', include('django.contrib.auth.urls')),
       url('update/', views.update, name='update'),
       url('<profdis/', views.profdis, name='profdis'),
       url('<update_profile/', views.update_profile, name='update_profile'),
       url('register/', views.register, name='register'),
       url('delete/', views.delete, name='delete'),


       url('signup/', views.signup, name='signup'),

]