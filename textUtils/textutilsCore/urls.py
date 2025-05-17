from django.urls import path,include
from .import views

urlpatterns =[
      path('',views.index2,name="index2"),
      path('about/',views.about,name="about"),
      path('contact/',views.Contact,name="contact"),
      path('analyze/',views.analyze,name="analyze")
]