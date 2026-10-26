from django.urls import path
from Basic import views

urlpatterns = [
    path('sum/',views.sum,name="sum"),
    path('Calculator/',views.calc,name="calculator"),
]
