from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .filters import ProjectFilter
from .serializers import ProjectSerializer
from .models import Project
# Create your views here.


@api_view(['GET'])
def get_all_projects(request):
    # projects = Project.objects.all()
    filterSet = ProjectFilter(request.GET,queryset=Project.objects.all().order_by('id'))
    count = filterSet.qs.count()
    resPage =9
    paginator = PageNumberPagination()
    paginator.page_size =resPage
    query_Set =paginator.paginate_queryset(filterSet.qs,request)
    serializer = ProjectSerializer(query_Set,many=True)
    return Response({"projects":serializer.data,"perPage":resPage,"totalProjects":count})

@api_view(['GET'])
def get_projects_detail(request,pk):
    project=get_object_or_404(Project,id=pk)
    serializer =ProjectSerializer(project,many=False)
    return Response({"projects":serializer.data})
