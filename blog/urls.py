from django.conf.urls import url
from blog import views


app_name = 'blog'

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^posts/(?P<pk>\d+)', views.DetailView, name='detail'),
    url(r'^addcomment/(?P<pk>\d+)', views.AddComment.as_view(), name='add-comment'),

]