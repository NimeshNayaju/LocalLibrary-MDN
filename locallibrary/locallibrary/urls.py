from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]


# Use include() to add URLS from the catalog application and authentication system
from django.conf.urls import include

urlpatterns += [
	path('catalog/', include('catalog.urls')),
]

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView

urlpatterns += [
	path('', RedirectView.as_view(url='/catalog/')),
]


# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Add Django site authentication
urlpatterns += [
	path('accounts/', include('django.contrib.auth.urls'))
]