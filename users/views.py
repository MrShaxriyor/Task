from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SignupSerializer, EmailLoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


@api_view(['POST'])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created"})
    return Response(serializer.errors)


class EmailLoginView(TokenObtainPairView):
    serializer_class = EmailLoginSerializer