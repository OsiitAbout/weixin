"""FreeSpoon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
import business.views

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/',include('allauth.urls')),
    url(r'^login_home/$', business.views.login_home_pag,name='login_home'),
    url(r'^login_order_details/$',business.views.login_order_details,name='login_order_details'),
    url(r'^login_order_list/$',business.views.login_order_list,name='login_order_list'),
    url(r'^bulk/$',business.views.bulks,name='bulk'),
    url(r'^datasource/ajaxsource/api/$', business.views.MyDataView.as_view(), name='ajax_source_api'),
    url(r'^datasource/order/api/$',business.views.OrderDataView.as_view(),name='ajax_order_api'),

    url(r'^ceshi/$',business.views.ceshi,name='ceshi'),
    url(r'^location/$',business.views.location,name='location'),   
    url(r'^wechat/', include('wechat.urls')),
    url(r'^MP_verify_mxqdYEZf8FuVDLUT.txt', views.mp_verify, name='mp_verify'),

]
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

