from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ProjectsListView, ProjectsDetailView

urlpatterns = [
    path('', ProjectsListView, name='project_list'),
    path('<int:pk>/', ProjectsDetailView.as_view(), name='project_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
