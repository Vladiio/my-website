from django.conf.urls import url
from blog import views


app_name = 'blog'

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^page/(\d+)/$', views.IndexView, name='paginator'),
    url(r'^posts/(?P<pk>\d+)/', views.DetailView, name='detail'),
    url(r'^category/(?P<pk>\d+)/', views.CategoryView, name='category'),
    url(r'^category/(?P<pk>\d+)/page/(?P<page_number>\d+)', views.CategoryView, name='category-pag'),
    url(r'^addcomment/(?P<pk>\d+)/', views.AddComment.as_view(), name='add-comment'),

]