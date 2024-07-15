from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    description= models.TextField(max_length=1000)
    icon = models.ImageField(upload_to='icons/', default='icons/default-icon.png',blank=True,null=True)

    def __str__(self) :
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    description= models.TextField(max_length=1000)
    profile_pic = models.ImageField(        upload_to='team_photos/', default='team_photos/default-employee.webp',blank=True,null=True)
    job_title = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    behance = models.CharField(max_length=100)

    def __str__(self) :
        return self.name

class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    review= models.TextField(max_length=1000)
    profile_pic = models.ImageField(upload_to='testi_photos/', default='team_photos/default-employee.webp',blank=True,null=True)
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)

    def __str__(self) :
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description= models.TextField(max_length=3000)
    blog_image = models.ImageField(upload_to='blogs/', default='blogs/default_blog.png',blank=True,null=True)

    def __str__(self) :
        return self.title
    