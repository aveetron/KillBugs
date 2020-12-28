from rest_framework import serializers

from BugTrackingTool.models import Bug, Member, Project, Status


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

class BugSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bug
        fields = '__all__'
