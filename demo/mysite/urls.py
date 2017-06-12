from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('mysite.views',
                       url(r'^$', 'index'),
                       )