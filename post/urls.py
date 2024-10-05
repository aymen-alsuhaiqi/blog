from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('add-posts',views.add_post,name='add-posts'),
    path('add-comments/<int:p_id>',views.add_comments,name='add-comments'),
]