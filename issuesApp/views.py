from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication


from issuesApp.models import Issue
from issuesApp.serializers import IssueSerialixer, Loginserializer, RegisterSerializer

# Create your views here.

@api_view(['POST'])
def login(request):
    data = request.data
    serializer = Loginserializer(data = data,)
    if serializer.is_valid():
        data = serializer.validated_data
        return Response({"message": "user loggedin successfully"})

    return Response(serializer.errors)


@api_view(["GET"])
def home(request):
    response = {
        'status' : "success",
        'message' : "we are live, let gooooooo!"
    }
    return Response(response)

class IssuesApi(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        objs = Issue.objects.all()
        serializer = IssueSerialixer(objs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = IssueSerialixer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
    
    
    def patch(self, request):
       data = request.data
       obj = Issue.objects.get(id = data['id'])
       serializer = IssueSerialixer(obj, data = data, partial = True)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

       return Response(serializer.errors)
    def delete(self, request):
        data = request.data
        obj = Issue.objects.get(id = data['id'])
        obj.delete()
        return Response({"message": "Issue deleted successfully"})

@api_view(['GET', 'POST', 'DELETE', 'PATCH'])
def issues(request):
    if request.method == 'GET':
        objs = Issue.objects.all()
        serializer = IssueSerialixer(objs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = IssueSerialixer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Issue.objects.get(id = data['id'])
        serializer = IssueSerialixer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
    else:
        if request.method == 'DELETE':
            data = request.data
            obj = Issue.objects.get(id = data['id'])
            obj.delete()
            return Response({"message": "Issue deleted successfully"})
        

class IssuesViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerialixer
    queryset = Issue.objects.all()

    def list(self, request):
        search = request.GET.get('agent_id')
        queryset = self.queryset
        if search:
            queryset = queryset.filter(agent_id=search)

        serializer = IssueSerialixer(queryset, many=True)
        return Response({'status': '200', 'data': serializer.data}, status = status.HTTP_200_OK)


class Register(APIView):  
    authentication_classes = []  # No authentication required
    permission_classes = [AllowAny]  
    
    def post(self, request):        
        data = request.data
        serializer = RegisterSerializer(data= data)
        if not serializer.is_valid():
            return Response({'success': False, 'message': 'Registration failed', 'error': serializer.errors}, status= status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'message': 'user created successfully', 'data': serializer.data}, status= status.HTTP_201_CREATED)
        
class LoginApi(APIView):
    authentication_classes = []  # No authentication required
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        serializer = Loginserializer(data = data)
        if not serializer.is_valid():
           return Response({'success': False, 'message': 'Login failed', 'error': serializer.errors}, status= status.HTTP_400_BAD_REQUEST)

        user = authenticate(email = serializer.data['email'], password = serializer.data['password'])

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'success': True, 'message': 'user logged successfully', 'token': str(token)}, status= status.HTTP_201_CREATED)        
