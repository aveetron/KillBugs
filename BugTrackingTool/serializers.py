from rest_framework import serializers
from BugTrackingTool.models import Member, Project, Status, Bug




class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = '__all__'