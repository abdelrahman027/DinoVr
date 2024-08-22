from django.db import models

# Create your models here.

class Category(models.TextChoices):
    Campaigns360="360 Campaigns"
    ANIMATION3D="3D Animation"
    ANIMATION2D="2D Animation"
    Media_Production="Media Production"
    Digital_Marketing="Digital Marketing"



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