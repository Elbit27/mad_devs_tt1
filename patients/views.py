from rest_framework import generics
from . import permitions, serializers
from .models import Patient


class PatientListAPIView(generics.ListAPIView):
    queryset = Patient.objects.all()
    permission_classes = [permitions.IsDoctor,]

    def get_serializer_class(self):
        return serializers.PatientListSerializer