from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from issuesApp.models import Issue
from issuesApp.serializers import IssueSerialixer, Loginserializer

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
