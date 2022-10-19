from rest_framework.views import APIView, status
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import User

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class CreateUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = User.objects.create(**serializer.data)
                
            return Response(UserSerializer(user).data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class LoginView(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token':token.key
        })