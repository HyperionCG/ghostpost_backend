from django.conf.urls import include, url

from ghost_app.views import VoteChoiceViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'vote', VoteChoiceViewSet, basename='vote')

urlpatterns = [
    url(r"^api/", include(router.urls))
]
