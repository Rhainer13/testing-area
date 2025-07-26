from django.urls import path
from . import views

urlpatterns = [
    path('report/victim/', views.victim_step, name='victim_step'),
    path('report/incident/', views.incident_step, name='incident_step'),
    path('report/perpetrator/', views.perpetrator_step, name='perpetrator_step'),
]