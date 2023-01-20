from django.urls import path
from . import views
app_name='fb'

urlpatterns = [
    path('',views.home, name='home'),
    path('/page',views.page, name='page'),
    path('/forget',views.forget, name='forget'),
        path('/craa',views.craa, name='craa')
   
]