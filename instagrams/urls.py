from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'instagram'),
    url(r'^search/', views.search_results, name='search_results'),
    # url(r'^new/user$', views.new_user, name='new-user'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
