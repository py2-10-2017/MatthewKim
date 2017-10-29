from django.conf.urls import url
from . import views

urlpatterns=[
    (url(r'^ninjagold$',views.index)),
    (url(r'^ninjagold/process$',views.process)),
    (url(r'^ninjagold/clear$',views.clear))
]
