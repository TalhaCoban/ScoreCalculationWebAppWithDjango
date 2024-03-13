from django.contrib import admin
from django.urls import path, include
from HedefiniTuttur.wiews import index, nonuseryks, nonuserlgs, AAsystem
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name = "index"),
    path("user/", include("user.urls")),
    path("nonuseryks", nonuseryks, name = "nonuseryks"),
    path("YKS/", include("YKS.urls")),
    path("nonuserlgs", nonuserlgs, name = "nonuserlgs"),
    path("LGS/", include("LGS.urls")),
    path("Mean_AA/",include("Mean_AA.urls")),
    path("AAsystem", AAsystem, name = "AAsystem"),
    path("Mean_A1/",include("Mean_A1.urls")),
    path("A1system", AAsystem, name = "A1system"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
