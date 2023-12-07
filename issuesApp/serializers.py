from rest_framework import serializers
from .models import Issue
import uuid

class Loginserializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class IssueSerialixer(serializers.ModelSerializer):
    id = serializers.UUIDField(default=uuid.uuid4, read_only=True)

    class Meta:
        model = Issue
        exclude = ['agent_response']
        # fields = '__all__'

    def validate(self, data):
        
       special_characters = "!@#$%^&*()_-./;<=>|,?|~"
       if any (c in special_characters for c in data['unit_no']):
           raise serializers.ValidationError('Invalid character in unit number field')
       return data