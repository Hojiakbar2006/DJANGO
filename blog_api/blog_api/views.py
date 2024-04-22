from .serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .permissions import IsAuthorOrReadonly


class PostList(ListCreateAPIView):
    permission_classes = (IsAuthorOrReadonly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadonly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
