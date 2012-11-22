from django.conf.urls import patterns, include, url

from django.conf.urls.defaults import *
from django.conf import settings

from media_tree.models import FileNode
from media_tree.contrib.views.detail.image import ImageNodeDetailView
from media_tree.contrib.views.listing import FileNodeListingView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^weblog/', include('zinnia.urls')),
                       url(r'^comments/', include('django.contrib.comments.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),              
                       url(r'^', include('cms.urls')),
                       url(r'^admin/tagging/autocomplete', include('pagetags.urls')),
#                       (r'^images/(?P<pk>\d+)/$', ImageNodeDetailView.as_view(
#            queryset=FileNode.objects.get(path='Taina').get_descendants()
#            )),
                       #(r'^listing/', FileNodeListingView.as_view(
#            queryset=[FileNode.objects.get(path='taina')],
#            list_max_depth=2
#            )),
                       )


if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
