from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AghjhViewSet, AhkjViewSet, LhkjViewSet, SgchgViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("lhkj", LhkjViewSet)
router.register("sgchg", SgchgViewSet)
router.register("aghjh", AghjhViewSet)
router.register("ahkj", AhkjViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
