from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.index,name="index"),
    path('user/<str:username>', views.user_bio,name="user_bio"),
    path('top_comment', views.top_comment,name="top_comment"),
    path('likes/<int:postid>',views.likes_post,name='likes_post'),
    path('create/post', views.add_post, name='add_post'),
    path('edit/<str:username>', views.edit_profile, name='edit_profile'),
]