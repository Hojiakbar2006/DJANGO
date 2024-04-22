from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from .models import Post, Rating
from .serializers import RatingSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        post_id = self.kwargs.get('pk', None)  # Use 'pk' to get the post ID

        if user_id:
            return Post.objects.filter(author=user_id)

        if post_id:
            # Retrieve a single post based on the ID
            return Post.objects.filter(pk=post_id)

        return Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@api_view(['POST'])
def rate_post(request, post_id):
    try:
        # Post id orqali Post obyektini topish
        post = Rating.objects.get(id=post_id)
    except Rating.DoesNotExist:
        return Response({'message': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    # Foydalanuvchi tomonidan berilgan reyting qiymati
    user_rating = request.data.get('rating')

    # Foydalanuvchi reytingini tekshirish
    if not isinstance(user_rating, int) or user_rating < 1 or user_rating > 5:
        return Response({'message': 'Yaroqsiz qiymat'}, status=status.HTTP_400_BAD_REQUEST)

    # Foydalanuvchi tomonidan beringan reyting obyektini topish
    rating_instance, created = Rating.objects.get_or_create(
        user=request.user, post=post)

    # Foydalanuvchi reytingini yangilash
    rating_instance.rating = user_rating
    rating_instance.save()

    # Rating obyektini serializer orqali JSON formatga o'tkazib berish
    serializer = RatingSerializer(rating_instance)

    return Response(serializer.data, status=status.HTTP_201_CREATED)
