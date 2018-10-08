from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'instagram'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^accounts/edit/',views.edit_profile, name='edit_profile'),
     url(r'^upload/$', views.upload_image, name='upload_image'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
