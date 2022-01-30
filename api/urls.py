from django.urls import path, include
from django.views.generic import RedirectView

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from api.views.direct import (
    LoginsView, CidView, UrlsView,
)

urlpatterns = (
    path('', RedirectView.as_view(pattern_name='swagger-ui', permanent=False)),

    # Swagger and schema
    path('doc', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema', SpectacularAPIView.as_view(), name='schema'),

    # Logins, Cid, Urls
    path('logins', LoginsView.as_view({'get': 'list'}), name='logins'),
    path('cid', CidView.as_view({'get': 'list'}), name='cid'),
    path('urls', UrlsView.as_view({'get': 'list'}), name='urls'),
)
