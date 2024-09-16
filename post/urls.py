from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('add-posts',views.add_post,name='add-posts'),
]