from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, TeacherViewSet, home

# ✅ DRF router for APIs
router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)

urlpatterns = [
    path('', home, name='home'),        # Home page
    path('api/', include(router.urls)), # API endpoints
]
