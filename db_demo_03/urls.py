from django.conf.urls import url
from . import index

urlpatterns = [
    url('index', index.index),
]