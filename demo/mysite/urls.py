from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('mysite.views',
                       url(r'^$', 'index'),
                       url(r'^login$', 'user_login'),
                       url(r'^login_check$', 'login_check'),
                       url(r'^registration$', 'registration'),
                       url(r'^logout$', 'user_logout')
                       )