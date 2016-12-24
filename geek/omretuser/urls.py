from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup/$', views.signup,name='signup'),
    url(r'^signup/submit/$',views.signup_submit),
    url(r'^signup/comfirm/$',views.signup_comfirm),
    url(r'^signin/', views.signin,name='signin'),
]
