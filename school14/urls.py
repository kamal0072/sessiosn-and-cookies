from django.contrib import admin
from django.urls import path
from poll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #urls for simple cookies
    # path('setcookie', views.set_cookie, name='set_cookie'),
    # path('getcookie', views.get_cookie, name='get_cookie'),
    # path('delcookie', views.delcookies, name='del_cookie'),

    #url for signed cookies
    # path('setsignedcookie/', views.set_signed_cookie, name='setsignedcookie'),
    # path('getsignedcookie/', views.get_signed_cookie, name='getsignedcookie'),
    # path('delsignedcookie/', views.del_signed_cookie, name='delsignedcookie'),


    #session urls
    path('setsession/', views.set_session, name='setsession'),
    path('getsession/', views.get_session, name='getsession'),
    path('delsession/', views.del_session, name='delsession'),
]
