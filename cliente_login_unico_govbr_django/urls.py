from django.urls import path, include

urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    path('', include('core.urls')),
    path(r'^accounts/', include('django.contrib.auth.urls')),
]
