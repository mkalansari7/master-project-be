from django.urls import path, include
from semesters.views import SemesterListSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("semester", SemesterListSet)

urlpatterns = [
    # ? auth 
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),

    # ? Semester
    path("", include(router.urls)),
    
]
