from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer, UserMiniSerializer


class ProfileViewSet(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except Exception as e:
            raise e

        return Response(UserSerializer(user).data)

    def update(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except Exception as e:
            raise e

        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()

        return Response({"message": "Success", "data": serializer.data})

    @action(detail=False, methods=['get'])
    def get_user_data(self, request):
        user_id = request.query_params.get("user_id", None)
        try:
            user = User.objects.get(id=user_id)
        except Exception as e:
            raise "Profile does not exist, uebok"

        return Response(UserMiniSerializer(user).data)
