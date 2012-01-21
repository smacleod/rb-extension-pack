from django.conf.urls.defaults import patterns, include


urlpatterns = patterns('rbautoreviewer.views',
    (r'^$', 'configure')
)
