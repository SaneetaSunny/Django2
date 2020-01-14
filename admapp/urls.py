from django.views.generic import TemplateView
from django .urls import path
from admapp import views

urlpatterns=[
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('login/',TemplateView.as_view(template_name='login.html'),name='login'),
    path('faculty-login/',TemplateView.as_view(template_name='faculty-login.html'),name='faculty-login'),
    path('student-leave/',TemplateView.as_view(template_name='student-leave.html'),name='student-leave'),
    path('assessment/',TemplateView.as_view(template_name='assessment.html'),name='assessment'),
    path('attendence_1/',TemplateView.as_view(template_name='attendence_1.html'),name='attendence_1'),
    path('faculty-profile/',TemplateView.as_view(template_name='faculty-profile.html'),name='faculty-profile'),
    path('faculty-profile-edit/',TemplateView.as_view(template_name='faculty-profile-edit.html'),name='faculty-profile-edit'),
    path('leave-forwarded/',TemplateView.as_view(template_name='leave-forwarded.html'),name='leave-forwarded'),
    path('leave-rejected/',TemplateView.as_view(template_name='leave-rejected.html'),name='leave-rejected'),
    path('faculty-profile',views.fac_profile,name='faculty-profile'),
    path('faculty-profile-edit',views.fac_pro_view,name='faculty-profile-edit'),
    path('signin',views.authentication,name='signin'),
    path('update',views.fac_profile_edit,name='fac_profile_edit'),
    path('student-leave',views.viewleave,name='student-leave'),
    path('approve',views.leaveapprove,name='approve_leave'),
    path('assess',views.submit_assessment,name='submit_assmnt'),
    path('attendence_1',views.submit_att,name='submit_att'),
    
    
]