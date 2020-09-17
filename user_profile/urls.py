#from .patterns import  *
from .views import  *
from .patterns import *



from django.urls import path

app_name='user_profile'

urlpatterns = [
    path('signup/',CreateUser.as_view(),name='signup'),
    path('login/',Login.as_view(),name='login'),
    path('get_profile/',getyourprofile),
    path('get_profile/',getyourprofile),
    path('createprofile/',createprofile,name='createprofile'),
    path('update_profile/',update_profile),
    path('get_interest/',get_interest_list),
    path('create_interest/',get_interest_list),
    path('update_interest/<int:pk>/',update_interest_list),
    path('delete_interest/<int:pk>/',delete_interest_list),
    path('mutual_interst_profile/', Mutual_interst.as_view()),
    path('follow_people/',follow),
    path('youfollowing_profile/',youfollowing_profile),
    path('create_post/',PostsView.as_view()),
    path('see_posts/',PostsView.as_view()),
    path('unfollow/<int:pk>/',unfollow)
]