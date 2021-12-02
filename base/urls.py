from django.urls import path
from . import views

urlpatterns = [
    path('paco/', views.home, name='home'),

    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),

    path('service/', views.service, name='service'),

    path('project/', views.project, name='project'),
    path('project_detail/<int:post_id>/', views.project_detail, name='project_detail'),

    path('register/<int:event_id>/', views.register, name='register'),
    path('', views.member, name='member'),
    path('student/', views.student, name='student'),
    # path('createStudent/', views.createStudent, name='createStudent'),
    path('gestionVol/', views.getVolunteer, name='gestionVol'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('sendmail/', views.sendmail, name='sendmail'),
]
