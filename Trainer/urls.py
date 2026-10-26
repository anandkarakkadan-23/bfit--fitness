from django.urls import path,include
from Trainer import views

app_name="Trainer"
urlpatterns =[
    
    path('Homepage/',views.homepage,name="Homepage"),
    path('TrainerProfile/',views.trainerprofile,name="TrainerProfile"),
    path('EditProfile/',views.editprofile,name="EditProfile"),
    path('ChangePassword/',views.changepassword,name="ChangePassword"),
    path('Complaint/',views.complaint,name="Complaint"),
    path('AssignedList/',views.assignedlist,name="AssignedList"), 
    path('diet/<int:assid>',views.diet,name="diet"), 
    path('plan/',views.plan,name="plan"), 
    path('ViewDiets/<int:dpid>',views.viewdiets,name="ViewDiets"), 
    path('deletedid/<int:did>',views.deletedid,name="deletedid"), 
    path('logout/',views.logout,name="logout"),
    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    # path('ajaxphoto/',views.ajaxphoto,name="ajaxphoto"),
    path('clearchat/',views.clearchat,name="clearchat"),
    
]