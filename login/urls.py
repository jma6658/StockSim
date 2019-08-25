from django.urls import path, include
from . import gettoken, views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('login', views.LoginView)

urlpatterns = [
    path('', include(router.urls)),
    path('login', gettoken.processlogin),
    path('register', gettoken.processregister),
    path('logout', gettoken.processlogout)
]
