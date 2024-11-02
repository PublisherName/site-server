from django.urls import path

from . import views


urlpatterns = [
    path("", views.FaqViewSet.as_view({"get": "list"}), name="list all faq"),
]
