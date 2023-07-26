from django.urls import path
from app3.views import *

urlpatterns =[
    path('fifth/',fifth,name='fifth'),
    path('sixth/',sixth,name='sixth'),
    path('nature/',nature,name='nature'),
]