from django.conf.urls import url
from SecurityApp import views

#Template urls

app_name = 'SecurityApp'

urlpatterns =[
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='user_login'),
]
