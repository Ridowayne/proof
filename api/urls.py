from issuesApp.views import home, issues, login, IssuesApi, IssuesViewSet, Register, LoginApi
from django.urls import include, path
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'agent-issues', IssuesViewSet, basename='agent-issues')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('register', Register.as_view()),
    path('home/', home),
    path('issues', issues),
    path('login', LoginApi.as_view()),
    path('IssuesApi', IssuesApi.as_view())
]
