
from django.conf.urls import include, url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.index, name="index"),

    # /music/71/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),

    # /music/71/favourite
    url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name="favourite"),
]
