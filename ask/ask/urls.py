
from django.conf.urls import patterns, url
from django.contrib.auth import views
#from qa.views import test
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('qa.views',
    url(r'^$', 'home', name='home'),
    #url(r'^login/$', views.login, ),
    url(r'^signup/', 'user_signup', name='user_signup'),
    url(r'^question/(?P<id>[0-9]+)/$', 'question_detail', name='question_detail'),
    url(r'^ask/.*$', 'ask', name='ask'),
    url(r'^popular/$', 'popular', name='popular'),
    url(r'^new/$', 'home', name='home'),
    url(r'^rating/$', 'rating', name='rating'),
    )
