from django.conf.urls import url
from loginsys import views


app_name = 'loginsys'

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
]