from rest_framework import serializers
from .models import Issue
import uuid
from django.contrib.auth.models import User
from .models import CustomUser
from django.db.models import Q

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
    
class RegisterSerializer(serializers.ModelSerializer):
     id = serializers.UUIDField(default=uuid.uuid4, read_only=True)
     full_name = serializers.CharField()
     email = serializers.EmailField()
     password = serializers.CharField()
     staff_id = serializers.CharField()
     region = serializers.CharField()
     ahq = serializers.CharField()
     location = serializers.CharField()
     staff_type = serializers.CharField() 

     class Meta:
         model = CustomUser
         fields = ('id','email', 'password', 'full_name', 'staff_id', 'region', 'ahq', 'location', 'staff_type')

    

     def validate(self, data):
        if 'email' in data and 'staff_id' in data:
            if CustomUser.objects.filter(Q(email=data['email']) | Q(staff_id=data['staff_id'])).exists():
                raise serializers.ValidationError('Email or agent number already exists')
        return data
     def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)