from django.shortcuts import render
from rest_framework.views import APIView
from BugTrackingTool.models import Member
from BugTrackingTool.serializers import MemberSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class MemberApiView(APIView):
    
    def get(self, request):
        allMember = Member.objects.all()
        serializer = MemberSerializer(allMember, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MemberSerializer(data = request.data)
        if serializer.is_valid():
            getMember = Member.objects.filter(name = request.data['name'])
            if getMember:
                return Response(status=status.HTTP_403_FORBIDDEN)
            else:
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)


class MemberDetailsApiView(APIView):

    def get(self,request, pk):
        member = Member.objects.get(pk=pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self, request, pk):
        member = Member.objects.get(pk=pk)
        serializer = MemberSerializer(member,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk):
        member = Member.objects.get(pk=pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)