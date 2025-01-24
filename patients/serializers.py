from rest_framework import serializers
from .models import Patient

class PatientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'full_name', 'date_of_birth',)
