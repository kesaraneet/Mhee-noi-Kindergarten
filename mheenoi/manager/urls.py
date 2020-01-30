from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('check/', include('check.urls')),
    path('report/', include('report.urls'))
    # path('manager/', include('manager.urls'))
]