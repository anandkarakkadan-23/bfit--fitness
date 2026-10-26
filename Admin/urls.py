from django.urls import path,include
from Admin import views

app_name="Admin"
urlpatterns = [
    path('District/',views.district,name="District"),
    path('deldistrict/<int:did>',views.deldistrict,name="deldistrict"),
    path('editdistrict/<int:eid>',views.editdistrict,name="editdistrict"),
    path('Category/',views.category,name="Category"),
    path('delcategory/<int:dcid>',views.delcategory,name="delcategory"),
    path('editcategory/<int:ecid>',views.editcategory,name="editcategory"),
    path('place/',views.place,name="place"),
    path('delplace/<int:did>',views.delplace,name="delplace"),
    path('editplace/<int:eid>',views.editplace,name="editplace"),
    path('subcategory/',views.subcategory,name="subcategory"),
    path('delsubcategory/<int:dsid>',views.delsubcategory,name="delsubcategory"),
    path('editsubcategory/<int:esid>',views.editsubcategory,name="editsubcategory"),
    path('Trainer/',views.trainer,name="Trainer"),
    path('GymPlan/',views.gymplan,name="GymPlan"),
    path('delgymplan/<int:gid>',views.delgymplan,name="delgymplan"),
    path('editgymplan/<int:hid>',views.editgymplan,name="editgymplan"),
    path('AdminRegistration/',views.adminregistration,name="AdminRegistration"),
    path('ViewUserComplaint/',views.viewusercomplaint,name="ViewUserComplaint"),
    path('reply/<int:rid>',views.reply,name="reply"),
    path('trainerreply/<int:tid>',views.trainerreply,name="trainerreply"),
    path('ViewTrainerComplaint/',views.viewtrainercomplaint,name="ViewTrainerComplaint"),
    path('ViewFeedback/',views.viewfeedback,name="ViewFeedback"),
    path('ViewAdmission/',views.viewadmission,name="ViewAdmission"),
    path('Viewusers/',views.viewusers,name="viewusers"),
    path('acceptuser/<int:accid>',views.acceptuser,name="acceptuser"),
    path('rejectuser/<int:rejid>',views.rejectuser,name="rejectuser"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('logout/',views.logout,name="logout"),
    path('assigntrainer/<int:admid>',views.assigntrainer,name="assigntrainer"),


]  