from django.urls import path, include
from semesters.views import SemesterListSet
from projects.views import ProjectListSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("semester", SemesterListSet)
router.register("project", ProjectListSet)


urlpatterns = [
    # ? auth 
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),

    # ? Semester & Project
    path("", include(router.urls)),

    
    
]
