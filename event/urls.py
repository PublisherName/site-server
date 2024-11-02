from django.urls import path

from . import views


urlpatterns = [
    path(
        "",
        views.EventReadonlyViewset.as_view({"get": "list"}),
        name="list-many-events",
    ),
    path(
        "<slug:slug>/",
        views.EventReadonlyViewset.as_view({"get": "retrieve"}),
        name="list-one-event",
    ),
]
