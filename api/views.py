from rest_framework import viewsets
from api.models import Prerequisites, PrerequisitesForm
from api.serializers import PrerequisitesSerializer, PrerequisitesFormSerializer

class PrerequisiteViewSet ( viewsets.ModelViewSet ):
    serializer_class = PrerequisitesSerializer
    queryset = Prerequisites.objects.all()
   
class PrerequisitesFormViewSet ( viewsets.ModelViewSet ):
    serializer_class = PrerequisitesFormSerializer
    queryset = PrerequisitesForm.objects.all()

# Create your views here.
