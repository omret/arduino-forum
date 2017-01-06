from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.forum,name='forum'),
    url(r'^forum/new$', views.forum_new),
    url(r'^forum/topic(\d+)$',views.topic_index),
]
