from django.urls import path
from django.urls import include
from django.contrib import admin

from docs.yasg.urls import urlpatterns as yasg_urls

from apps.shop.views.home import home_view
from apps.shop.views.call_back import PaymeCallBackAPIView


urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path("shop/", include("shop.urls")),
    path('payments/merchant/', PaymeCallBackAPIView.as_view()) # call back for merchant transactions
]

urlpatterns += yasg_urls
