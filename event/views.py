from rest_framework import permissions, viewsets

from . import models, serializers


class EventReadonlyViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.filter(is_draft=False)
    permission_classes = [
        permissions.AllowAny,
    ]
    lookup_field = "slug"
    lookup_url_kwarg = "slug"
