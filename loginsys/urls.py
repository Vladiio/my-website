from django.conf.urls import url
from loginsys import views


app_name = 'loginsys'

urlpatterns = [
    url(r'^login$', views.LoginView.as_view(), name='login'),
]