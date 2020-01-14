from django.views.generic import TemplateView
from django.urls import path
from student import views

urlpatterns=[
    path('home/',TemplateView.as_view(template_name='home.html'),name='home'),
    path('student-applied-leave/',TemplateView.as_view(template_name='student-applied-leave.html'),name='student-applied-leave'),
    path('student-assessment/',TemplateView.as_view(template_name='student-assessment.html'),name='student-assessment'),
    path('student-attendence/',TemplateView.as_view(template_name='student-attendence.html'),name='student-attendence'),
    path('student-edit/',TemplateView.as_view(template_name='student-edit.html'),name='student-edit'),
    path('student-leave-management/',TemplateView.as_view(template_name='student-leave-management.html'),name='student-leave-management'),
    path('student-profile/',TemplateView.as_view(template_name='student-profile.html'),name='student-profile'),
    path('stupro',views.stud_profile,name='student-profile'),
    path('studview',views.stud_pro_view,name='student-edit'),
    path('stud_profile_edit',views.stud_pro_edit,name='stud_profile_edit'),
    path('student-leave-management',views.stud_leave_apply,name='apply_leave'),
    path('student-assessment',views.stud_assmnt_view,name='student-assessment'),
    path('student-applied-leave',views.view_applied_leave,name='student-applied-leave'),
    path('student-attendence',views.view_attendance,name='student-attendence'),

]