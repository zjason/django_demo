from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('mysite.views',
                       url(r'^$', 'index'),
                       url(r'^login$', 'login'),
                       url(r'^login_check$', 'login_check')
                       )