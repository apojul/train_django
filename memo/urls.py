from django.conf.urls import url
from memo.views import welcome

urlpatterns = [
    url('', welcome)
]