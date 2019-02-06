from django.conf.urls import url
from car_app import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'car_app'

urlpatterns = [
	url(r'^new/model/$', views.model_new, name='model_new'),
	url(r'^model/(?P<pk>[0-9]+)/edit/$', views.model_edit, name='model_edit'),	
	url(r'^models/$', views.models, name='models'),
	url(r'^models/(?P<pk>[0-9]+)/$', views.model_detail, name='model_detail'),

	url(r'^new/number/$', views.number_new, name='number_new'),
	url(r'^number/(?P<pk>[0-9]+)/edit/$', views.number_edit, name='number_edit'),	
	url(r'^numbers/$', views.numbers, name='numbers'),
	url(r'^numbers/(?P<pk>[0-9]+)/$', views.number_detail, name='number_detail'),

	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),	
	url(r'^posts/$', views.posts, name='posts'),
	url(r'^post/(?P<pk>[0-9]+)/$',  views.post_detail, name='post_detail'), 

]


