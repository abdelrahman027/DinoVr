from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Service,Team,Blog,Testimonials,Faqs,Location
from .serializers import ServiceSerializer ,BlogSerializer ,TeamSerializer,TestimonialsSerializer,FaqsSerializer,LocationSerializer
# Create your views here.


@api_view(['GET'])
def get_all_services(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services,many=True)
    return Response({"services":serializer.data})

@api_view(['GET'])
def get_services_detail(request,pk):
    services = get_object_or_404(Service,id=pk)
    serializer = ServiceSerializer(services,many=False)

    return Response({"services":serializer.data})

@api_view(['GET'])
def get_all_teams(request):
    teams = Team.objects.all()
    serializer = TeamSerializer(teams,many=True)
    return Response({"teams":serializer.data})

@api_view(['GET'])
def get_all_testimonials(request):
    testimonials = Testimonials.objects.all()
    serializer = TestimonialsSerializer(testimonials,many=True)
    return Response({"testimonials":serializer.data})

@api_view(['GET'])
def get_all_blogs(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs,many=True)
    return Response({"blogs":serializer.data})

@api_view(['GET'])
def get_blogs_detail(request,pk):
    blogs = get_object_or_404(Blog,id=pk)
    serializer = BlogSerializer(blogs,many=False)

    return Response({"blogs":serializer.data})


@api_view(['GET'])
def get_all_faqs(request):
    faqs = Faqs.objects.all()
    serializer = FaqsSerializer(faqs,many=True)
    return Response({"faqs":serializer.data})

@api_view(['GET'])
def get_all_locations(request):
    locations = Location.objects.all()
    serializer = LocationSerializer(locations,many=True)
    return Response({"locations":serializer.data})