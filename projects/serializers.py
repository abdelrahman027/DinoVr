from rest_framework import serializers
from .models import Project,ProjectImage

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ('image',)


class ProjectSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    def get_images(self, project):
        return ProjectImageSerializer(project.project_images.all(), many=True).data
    class Meta: 
        model=Project
        fields="__all__"