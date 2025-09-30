from django.urls import path
from . import views

app_name = "faqs"

urlpatterns = [
    path("fyq/", views.faq_page, name="page"),     # Página HTML
    path("api/faqs", views.faqs_api, name="api"),  # Endpoint JSON
]
