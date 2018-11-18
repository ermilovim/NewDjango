from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addnewid$', views.addnewid, name='addnewid'),
    url(r'^check_exist_user_by_id$', views.check_exist_user_by_id, name="check_exist_user_by_id"),
]