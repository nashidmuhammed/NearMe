from django.urls import path
from .import views
urlpatterns=[
    path('',views.open,name='open'),
    path('hom',views.hom,name='hom'),
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('regt',views.regt,name='regt'),
    path('registered',views.registered,name='registered'),
    path('log',views.log,name='log'),
    path('logout',views.logout,name='logout'),
    path('profile',views.profile,name='profile'),
    path('locadd',views.locadd,name='locadd'),
    path('success',views.success,name='success'),
    path('locview',views.locview,name='locview'),
    path('about',views.about,name='about'),
    path('view',views.view,name='view'),
    path('feed',views.feed,name='feed'),
    path('liked',views.liked,name='liked'),
    path('notification',views.notification,name='notification'),
    path('admins',views.admins,name='admins'),
    path('more',views.more,name='more'),
    path('approve',views.approve,name='approve'),
    path('reject',views.reject,name='reject'),
    path('fedview',views.fedview,name='fedview'),
    path('fedreplay',views.fedreplay,name='fedreplay'),
    path('trash',views.trash,name='trash'),
    path('change',views.change,name='change'),



]
