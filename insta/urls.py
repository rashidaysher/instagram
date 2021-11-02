from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns=[
    path('', views.home,name="home"),
    path('user/<str:username>', views.user_profile,name="user_profile"),
    path('add_comment', views.add_comment,name="add_comment"),
    path('like/<int:postid>',views.like_post,name='like_post'),
    path('create/post', views.add_post, name='add_post'),
    path('edit/<str:username>', views.edit_profile, name='edit_profile'),
    path('search/', views.search_profile, name='search'),
    path('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    path('follow/<to_follow>', views.follow, name='follow'),
]


    