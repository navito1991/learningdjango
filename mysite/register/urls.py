from django.urls import path,include

from register import views as v
urlpatterns = [

path("registering",v.register, name="register" ),
path('',include("django.contrib.auth.urls")),
]