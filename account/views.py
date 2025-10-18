from rest_framework import viewsets, permissions, status
from rest_framework.response import response
from django.contrib.auth.models import user
from .serializers import UserProfileSerializer

class Userprofileviewset(viewsets.Viewset):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def retrieve(self, request):
        serializer = UserProfileSerializer(self.get_object())
        return Response(serializer.data)

    def update(self, request):
        user = self.get_object()
        serializer = UserProfileSerializer(user, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request):
        user = self.get_object()
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_Ok)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)