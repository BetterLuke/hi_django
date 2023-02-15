from django.urls import path
from signup_api.views import Companies

urlpatterns = [path("", Companies.as_view())]
