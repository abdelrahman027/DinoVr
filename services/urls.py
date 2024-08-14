from django.urls import path,include


from . import views

urlpatterns = [
    path("services/",views.get_all_services,name="services"),
    path("services/<str:pk>/",views.get_services_detail,name="services-detail"),
    path("team/",views.get_all_teams,name="teams"),
    path("testimonials/",views.get_all_testimonials,name="testimonials"),
    path("blogs/",views.get_all_blogs,name="blogs"),
    path("blogs/<str:pk>",views.get_blogs_detail,name="blogs-detail"),
    path("faqs/",views.get_all_faqs,name="faqs"),
    path("locations/",views.get_all_locations,name="locations"),
]
