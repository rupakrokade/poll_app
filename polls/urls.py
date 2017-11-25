from django.conf.urls import url

from . import views

urlpatterns = [ 
    url(r'^home/$',views.index,name='index'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^register/$',views.register_view,name='register_view'),
    url(r'^logout/$',views.logout,name='logout'),
]

