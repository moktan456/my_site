from django.urls import path
from . import views
urlpatterns = [
    # urls when views defined as function 
    # path('',views.index,name='index'),
    # path('posts/',views.allPosts, name='posts'),
    # /posts/my-first-post
    # path('posts/<slug:slug>',views.post_detail, name='post-detail'),
    # urls when views defined as class 
    path("",views.StartingPageView.as_view(),name="starting-page"),
    path("posts/",views.AllPostsView.as_view(),name="posts"),
    path("posts/<slug:slug>",views.SinglePostView.as_view(),name="post-detail")

]
