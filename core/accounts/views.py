from django.shortcuts import render
from django.views.generic import TemplateView


class AuthorizationsView(TemplateView):
    template_name = "accounts/authorizations.html"
