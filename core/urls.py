from django.contrib import admin
from django.urls import path, include
from django.conf import settings                      # ← add
from django.conf.urls.static import static            # ← add

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("portfolio.urls")),           # your existing line
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # ← add