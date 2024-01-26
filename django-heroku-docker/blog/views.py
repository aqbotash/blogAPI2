from rest_framework import generics, status
from rest_framework.response import Response
from .models import Post, Comment
from django.contrib.auth.models import User
from .serializers import PostSerializer, CommentSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

class RegisterCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Manually handle password hashing
        password = serializer.validated_data['password']
        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            email=serializer.validated_data['email'],
            password=password,  # This will automatically hash the password
            first_name=serializer.validated_data['first_name'],
            last_name=serializer.validated_data['last_name'],
        )

        # Optionally, you can include logic to generate and return a token here

        headers = self.get_success_headers(serializer.data)

        return Response(
            {"user": serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )
    
class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    