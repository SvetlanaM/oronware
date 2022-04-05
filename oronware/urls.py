from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.utils.translation import gettext_lazy as _


admin.site.index_title = _('OronWare')
admin.site.site_header = _('My Site Administration')
admin.site.site_title = _('My Site Management')


urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
