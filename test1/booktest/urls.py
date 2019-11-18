from django.conf.urls import url
from booktest import views
urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^books/$', views.show_books),
    url(r'^books/(\d+)/$', views.detail),
    url(r'^create/$', views.create),
    url(r'^delete(\d+)/$', views.delete),
    url(r'^delete(\d+)/$',views.delete),
    url(r'^areas/',views.areas),
    url(r'^test_ajax/$',views.ajax_test),
    url(r'^ajax_handle/$',views.ajax_handle),
    url(r'^login/$',views.login),
    url(r'^login_check/$',views.login_check),
]
