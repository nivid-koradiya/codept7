
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    
]


urlpatterns+= staticfiles_urlpatterns() 
if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#DJANGO admin site settings
admin.site.site_header = "Codept7 Admin"
admin.site.site_title = "Codept7 Admin Site"
admin.site.index_title = "Welcome to Codept Analyzer Site"