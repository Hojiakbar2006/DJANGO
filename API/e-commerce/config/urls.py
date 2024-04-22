from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="APi E-commerce",
        default_version="v1",
        description="E-commerce",
        terms_of_service="",
        contact=openapi.Contact(email="hojiakbarnasriddinov2006@gmail.com"),
        license=openapi.License(name="BSD license")
    ),

    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include("products.urls")),
    re_path(r"swagger(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui')
]
