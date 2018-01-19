from django.conf.urls import url, include
from rest_framework import routers
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^groups/$', views.GroupList.as_view(), name='group-list'),
    url(r'^groups/(?P<pk>[0-9]+)/$', views.GroupDetail.as_view(), name='group-detail'),
    url(r'^permissions/$', views.PermissionList.as_view(), name='permission-list'),
    url(r'^permissions/(?P<pk>[0-9]+)/$', views.PermissionDetail.as_view(), name='permission-detail'),
    url(r'^datapull/$', views.DataPullIDList.as_view(), name='pull-list'),
    url(r'^datapull/(?P<pk>[0-9]+)/$', views.DataPullIDDetail.as_view(), name='pull-list-detail'),
    url(r'^datapull/details/$', views.DataPullDetailsCreate.as_view(), name='pull-detail-create'),
    url(r'^datapull/details/(?P<pullid>[0-9]+)/$', views.DataPullDetails.as_view(), name='pull-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)