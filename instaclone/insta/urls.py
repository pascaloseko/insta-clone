from django.conf.urls import url 
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
      url('^$',views.index, name='index'),
      url('^profile/',views.profile, name='profile'),
      url('^upload/',views.upload, name='upload')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)