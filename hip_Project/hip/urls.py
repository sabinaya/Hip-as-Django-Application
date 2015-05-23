from django.conf.urls import patterns, url
from hip import views

urlpatterns = patterns('',
	url(r'^$', views.game, name='game')
)