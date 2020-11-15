from rest_framework import mixins, viewsets, filters
from django_filters import rest_framework

from .models import Timeslot
from .serializers import TimeslotSerializer


class TimeslotViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = Timeslot.objects.all()
    serializer_class = TimeslotSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_fields = ('dentist', 'startTime', 'date', 'status')
