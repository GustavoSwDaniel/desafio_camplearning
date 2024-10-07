from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from desafio_camplearning import settings
from files.views import redirect_to_files

urlpatterns = [
    path('', redirect_to_files),
    path('admin/', admin.site.urls),
    path('files/', include('files.urls')),
    path('users/', include('users.urls'))   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
