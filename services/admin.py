from django.contrib import admin
from .models import Service,Blog,Team,Testimonials,Faqs

# Register your models here.

admin.site.register(Service)
admin.site.register(Blog)
admin.site.register(Team)
admin.site.register(Testimonials)
admin.site.register(Faqs)
