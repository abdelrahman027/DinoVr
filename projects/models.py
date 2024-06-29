from django.db import models

# Create your models here.

class Category(models.TextChoices):
    DRAWING3D="3D Drawing"
    DRAWING2D="2D Drawing"
    MEDIA_PRODUCTION="Media Production"
    ANIMATION="Animation"
    STORY_BOARDS="Story Boards"



class Project(models.Model):
    name= models.CharField(max_length=200)
    description= models.TextField(max_length=1000)
    category = models.CharField(max_length=40,choices=Category.choices)
    createAt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, 
    null=True, related_name='project_images')
    image = models.ImageField(null=True, blank=True,
    default='/project_photos/default_project.png',upload_to='project_photos/',)