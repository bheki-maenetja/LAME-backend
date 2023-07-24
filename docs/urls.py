from django.urls import path
from .views import SingleDoc, ManyDocs

urlpatterns = [
    path("", ManyDocs.as_view()),
    path("<int:pk>/", SingleDoc.as_view())
]