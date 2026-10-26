from django.urls import path,include
from Guest import views

app_name="Guest"
urlpatterns =[
    path('userregistration/',views.userregistration,name="userregistration"),
    path('ajaxplace/',views.ajaxplace,name="ajaxplace"),
    path('Login/',views.login,name="Login"),
    path('',views.index,name="index"),
]