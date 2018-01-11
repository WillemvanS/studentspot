#urls specific for studentspot

from django.conf.urls import url
from . import views

#see views.py for what the urls refer to
urlpatterns = [
    url(r'^$', views.show_calendar, name='show_calendar'),
    url(r'^$', views.homepage, name='homepage'),
]
