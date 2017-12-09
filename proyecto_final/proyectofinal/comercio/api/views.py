from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions

from  comercio.models import Burritos
from .pagination import StandardResultPagination
from .serializers import BurritosModelSerializer


class BurritosCreateAPIView(generics.CreateAPIView):
    serializer_class = BurritosModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BurritosListAPIView(generics.ListAPIView):
    serializer_class = BurritosModelSerializer
    pagination_class = StandardResultPagination

    def get_queryset(self, *args, **kwargs):
        qs = Burritos.objects.all().order_by("-tamano")
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                            Q(tamano__icontains=query) |
                            Q(precio__icontains=query)
                          )
        return qs
