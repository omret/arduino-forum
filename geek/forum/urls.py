from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^forum/$', views.forum,name='forum'),
    url(r'^forum/new$', views.forum_new),
    url(r'^token/$',views.token),
]
