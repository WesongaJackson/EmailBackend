from django.urls import path
from Accounts import  views
urlpatterns=[
    path('',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('login/',views.signin,name="login"),
    path('logout/',views.sign_out,name="logout"),
]