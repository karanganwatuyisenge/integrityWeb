from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='index'),
    # path('appointment',appointment,name='appointment'),
    path('dashboard1',dashboard1,name='dashboard1'),
    path('signup',registration,name='signup'),
    path('patientregistration',patientregistration,name='patientregistration'),
    path("login/", login_request, name="login"),
    path('showpatient/',showpatient,name='showpatient'),
    path('showemployee/',showemployee,name='showemployee'),
    # path('update/<int:id>',update,name='edit'),
    path('admindashboard',admindashboard,name='admindashboard')
]