from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^courses$',views.index),
    url(r'^courses/add$',views.add),
    url(r'^courses/(?P<course_id>\d+)/destroy$',views.destroy),
    url(r'^courses/(?P<course_id>\d+)/destroying$',views.destroying),

]
