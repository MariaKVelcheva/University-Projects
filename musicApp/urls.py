from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('musicApp.common.urls')),
    path('album/', include('musicApp.albums.urls')),
    path('profile/', include('musicApp.profiles.urls'))

]
