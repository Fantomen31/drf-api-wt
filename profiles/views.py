from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer
from drfapi.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    List all profiles
    No Create view (post method), as profile creation handled by django signals
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

class ProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()