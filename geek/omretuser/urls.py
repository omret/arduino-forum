from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup/', views.signup,name='signup'),
    url(r'^signupsubmit/$',views.signup_submit),
    url(r'^signupcomfirm/$',views.signup_comfirm),
    url(r'^signin/', views.signin,name='signin'),
    url(r'^signinsubmit/$',views.signin_submit),
]
