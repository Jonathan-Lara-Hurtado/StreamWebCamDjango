from django.urls import path
from stream import views

app_name = 'stream'

urlpatterns = [
    path('index/',views.livecam_feed,name='index'),
    path('',views.principal,name="index2"),
]