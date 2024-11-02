from rest_framework import serializers

from . import models


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faq
        fields = "__all__"
