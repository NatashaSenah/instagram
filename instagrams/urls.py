from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^instagram',views.welcome,name = 'instagram'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^accounts/edit/',views.edit_profile, name='edit_profile'),
    url(r'^upload/$', views.upload_image, name='upload_image'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^$', views.signup, name='registration_form'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^signup/$', views.signup, name='signup'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
