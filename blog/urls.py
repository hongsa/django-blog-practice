from django.conf.urls import url
from blog import views
from blog import views_cbv

urlpatterns = [
    # url(r'^$',views.index, name='index'),
    url(r'^$',views_cbv.index, name='index'),

    # url(r'^posts/$',views.post_list,name='post_list'),
    url(r'^posts/$',views_cbv.post_list ,name='post_list'),
    # url(r'^posts/(?P<pk>\d+)/$',views.post_detail, name='post_detail'),
    url(r'^posts/(?P<pk>\d+)/$',views_cbv.post_detail, name='post_detail'),
    # url(r'^posts/new/$',views.post_new,name='post_new'),
    url(r'^posts/new/$',views_cbv.post_new,name='post_new'),
    # url(r'^posts/(?P<pk>\d+)/edit/$',views.post_edit, name='post_edit'),
    url(r'^posts/(?P<pk>\d+)/edit/$',views_cbv.post_edit, name='post_edit'),
    url(r'^posts/(?P<pk>\d+)/delete/$',views.post_delete, name='post_delete'),
    # url(r'^posts/(?P<pk>\d+)/delete/$',views_cbv.post_delete, name='post_delete'),


]
