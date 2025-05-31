# from rest_framework import routers

# from rest_framework_nested import routers as nested_routers
from rest_framework_nested import routers


from django.urls import path, include

from api.views import (
    DepartementViewSet,
    IssueCategoryViewSet,
    IssueCommentViewSet,
    IssueViewSet,
)


router = routers.DefaultRouter()
router.register(r"categories", IssueCategoryViewSet, basename="issuecategory")
router.register(r"departments", DepartementViewSet, basename="department")
router.register(r"issues", IssueViewSet, basename="issue")

issues_router = routers.NestedSimpleRouter(router, "issues", lookup="issue")
issues_router.register("comments", IssueCommentViewSet, basename="issuecomment")


urlpatterns = [
    path("", include(router.urls)),
    path("", include(issues_router.urls)),
]
