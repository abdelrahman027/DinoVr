import django_filters

from .models import Project 
class ProjectFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    keyword =django_filters.CharFilter(field_name="name",lookup_expr="icontains")

    class Meta:
        model = Project
        fields = ["name", 'category']