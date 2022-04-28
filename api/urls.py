from django.urls import path, include
from semesters.views import SemesterListSet
from projects.views import ProjectListSet
from teams.views import TeamListSet
from criterias.views import CriteriaListSet
from evaluations.views import EvaluationListSet
from judges.views import JudgeListSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("semester", SemesterListSet)
router.register("project", ProjectListSet)
router.register("team", TeamListSet)
router.register("criteria", CriteriaListSet)
router.register("evaluation", EvaluationListSet)
router.register("judge", JudgeListSet)


urlpatterns = [
    # ? auth 
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),

    # ? Semester & Project
    path("", include(router.urls)),

    
    
]
