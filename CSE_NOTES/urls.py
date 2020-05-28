from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cryptography', views.cryptography, name="cnscl"),
    path('computergraphics', views.computergraphics, name="cg"),
    path('systemsofware', views.systemsofware, name="ss"),
    path('operatingsystem', views.operatingsystem, name="os"),
    path('operationalresearch', views.operationalresearch, name="opr"),
    path('python', views.python, name="pyth"),
    ]
