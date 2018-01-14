#urls specific for studentspot

from django.conf.urls import url
from . import views

#see views.py for what the urls refer to
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^calendar/$', views.show_calendar, name='show_calendar'),
    url(r'^addtogroup/$', views.add_to_group, name='add_to_group'),
    url(r'^$', views.homepage, name='homepage'),
]
