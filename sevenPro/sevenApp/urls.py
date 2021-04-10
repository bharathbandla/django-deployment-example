from django.conf.urls import url
from sevenApp import views

#Template Urls

app_name = 'sevenAppu'

urlpatterns = [
    url(r'^register/$', views.register_fun, name='regis'),
    url(r'^greegrow', views.gro_gree, name='gree'),
    url(r'^us_login', views.user_login_fun, name='cus_login'),
    url(r'^us_crt', views.cart_fun, name='crt')
]