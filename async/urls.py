from django.conf.urls import patterns, include, url

from django.contrib import admin
from rest_framework import routers
from hacker import views

router = routers.DefaultRouter()
router.register(r'api/hacker', views.HackerViewSet)
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'async.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include(router.urls)),
                       url(r'^api_auth/',
                           include(
                               'rest_framework.urls',
                               namespace='rest_framework')),
                       url(r'^auth/',
                           include('rest_framework_social_oauth2.urls')),
                       )
