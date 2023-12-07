from issuesApp.views import home, issues, login, IssuesApi, IssuesViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'issues', IssuesViewSet, basename='issues')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('home/', home),
    path('issues', issues),
    path('login', login),
    path('IssuesApi', IssuesApi.as_view())
]
