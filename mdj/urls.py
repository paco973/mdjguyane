from urllib import request

import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('blog/', include('blog.urls')),
    path('donation/', include('don.urls')),
    path('payment/', include('payment.urls')),
    path('services/', include('service.urls')),
    path('store/', include('store.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    

