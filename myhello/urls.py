from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('',views.HelloAPIView.as_view(),name='index'),

    path('add',views.Add_post.as_view(),name='add_post'),
    path('list',views.List_post.as_view(),name='list_post'),

    # path('list_user',views.List_user.as_view(),name='list_user'),
    # path('',views.HelloAPIViewDecorator,name='index'),
]