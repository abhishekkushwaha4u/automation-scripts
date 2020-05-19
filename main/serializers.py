from rest_framework import serializers
from .models import Script

class ScriptSerializer(serializers.ModelSerializer):
    model = Script
    