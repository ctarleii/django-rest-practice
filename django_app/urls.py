from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('rest_app.urls')),
    path('auth/', include('accounts.urls'))
]
