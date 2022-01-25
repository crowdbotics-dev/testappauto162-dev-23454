from rest_framework import viewsets
from home.models import Aghjh, Ahkj, Lhkj, Sgchg
from .serializers import (
    AghjhSerializer,
    AhkjSerializer,
    LhkjSerializer,
    SgchgSerializer,
)
from rest_framework import authentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from home.api.v1.serializers import (
    SignupSerializer,
    UserSerializer,
)


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})


class LhkjViewSet(viewsets.ModelViewSet):
    serializer_class = LhkjSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Lhkj.objects.all()


class SgchgViewSet(viewsets.ModelViewSet):
    serializer_class = SgchgSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Sgchg.objects.all()


class AghjhViewSet(viewsets.ModelViewSet):
    serializer_class = AghjhSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Aghjh.objects.all()


class AhkjViewSet(viewsets.ModelViewSet):
    serializer_class = AhkjSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Ahkj.objects.all()
