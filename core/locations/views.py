from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Location

class LocationsView(TemplateView):
    template_name = "locations/locations.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Location.objects.all()
        return context
