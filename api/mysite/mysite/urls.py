from django.urls import path, include

urlpatterns = [
    path("api/", include("api.urls")),
    path("", include("api.urls")),  # add this line
]
