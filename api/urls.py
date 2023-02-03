from rest_framework.routers import DefaultRouter
from api.views import PrerequisitesFormViewSet, PrerequisiteViewSet

router = DefaultRouter()

router.register('api/prerequisite', PrerequisiteViewSet)
router.register('api/prerequisiteForm', PrerequisitesFormViewSet)
#Otras rutas

urlpatterns = []

urlpatterns += router.urls