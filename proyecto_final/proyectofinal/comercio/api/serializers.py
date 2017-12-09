from django.utils.timesince import timesince
from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer
from comercio.models import Burritos

class BurritosModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    class Meta:
        model = Burritos
        fields = [
            'id',
            'user',
            'tamano',
            'descripcion',
            'ingredientes',
            'precio',
            'date_display',
            'timesince'
        ]

    def get_date_display(self, obj):
        return obj.creado.strftime("%b %d %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.creado) + " ago"
