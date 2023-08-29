from rest_framework import serializers
from .models import ProcessMaster


class ProcessMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessMaster
        fields = '__all__'
