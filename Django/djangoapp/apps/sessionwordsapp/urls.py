from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^session_word$',views.session_word),
    url(r'^session_word/add$',views.add),
    url(r'^session_word/clear$',views.clear)
]
