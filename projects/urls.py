from django.urls import path,include
from . import views



urlpatterns = [
    path("projects/",views.get_all_projects,name="projects"),
    path("projects/<str:pk>/",views.get_projects_detail,name="projects_detail")
]

