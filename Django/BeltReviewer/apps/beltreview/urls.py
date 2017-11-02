from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^books$',views.books),
    url(r'^books/add$',views.add),
    url(r'^(?P<book_num>\d+)/add/review$',views.addreview),
    url(r'^books/add/process$',views.addprocess),
    url(r'^books/(?P<book_num>\d+)$',views.book),
    url(r'^users/(?P<user_num>\d+)$',views.user),
    url(r'^register$',views.register) ,
    url(r'^login$',views.login) ,
    url(r'^logout$',views.logout)
]
