from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from . import models, serializers


# Create your views here.
class FaqViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = models.Faq.objects.filter().order_by("position")
    serializer_class = serializers.FaqSerializer
