from django.urls import path,include
from User import views

app_name="User"
urlpatterns =[
    path('Homepage/',views.homepage,name="Homepage"),

    path('UserProfile/',views.userprofile,name="UserProfile"),
    path('EditProfile/',views.editprofile,name="EditProfile"),
    path('ChangePassword/',views.changepassword,name="ChangePassword"),

    path('FeedBack/',views.feedback,name="feedback"),
    path('complaint/',views.complaint,name="complaint"),

    path('ViewGymplans/',views.ViewGymplans,name="ViewGymplans"),

    path('Admission/<int:id>',views.admission,name="Admission"),
    path('deladmission/<int:adid>/<int:id>',views.deladmission,name="deladmission"),

    path('delcomplaint/<int:did>',views.delcomplaint,name="delcomplaint"),
    path('delfeedback/<int:dfid>',views.delfeedback,name="delfeedback"),

    path('payment/<int:id>',views.payment,name="payment"),
    path("payment/<int:id>",views.payment,name="payment"),
    path('loader/',views.loader, name='loader'),
    path('paymentsuc/',views.paymentsuc, name='paymentsuc'),

    path('MyAdmission/',views.MyAdmission, name='MyAdmission'),

    # path('admision/',views.admision,name="admision"),
    # path('deladmission/<int:adid>',views.deladmission,name="deladmission"),

    path('MyDiet/<int:dmid>',views.mydiet,name="MyDiet"),
    path('delmydiet/<int:deid>',views.delmydiet,name="delmydiet"),

    path('Viewassign/',views.Viewassign,name="Viewassign"),
    path('logout/',views.logout,name="logout"),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    # path('ajaxphoto/',views.ajaxphoto,name="ajaxphoto"),
    path('clearchat/',views.clearchat,name="clearchat"),

    #gallery
    path('workout/',views.workout,name="workout"),
    path('musclegaining/',views.musclegaining,name="musclegaining"),
    path('Workouts/',views.workouts,name="Workouts"),
    path('ABSworkout/',views.absworkout,name="absworkout"),
    path('Legsworkout/',views.Legsworkout,name="Legsworkout"),
    path('Fullbody/',views.fullbody,name="Fullbody"),
    path('Cardio/',views.cardio,name="Cardio"),
    path('shoulder/',views.shoulder,name="shoulder"),
    
] 

