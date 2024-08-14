from rest_framework import serializers
from .models import Service,Blog,Team,Testimonials,Faqs,Location


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model= Service
        fields="__all__"


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model= Blog
        fields="__all__"


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model= Team
        fields="__all__"


class TestimonialsSerializer(serializers.ModelSerializer):

    class Meta:
        model= Testimonials
        fields="__all__"


class FaqsSerializer(serializers.ModelSerializer):

    class Meta:
        model= Faqs
        fields="__all__"

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model= Location
        fields="__all__"
