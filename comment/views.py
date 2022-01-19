from rest_framework.viewsets import ModelViewSet

from comment.models import Comment
from comment.serializers import CommentSerializer


class CommentViewset(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
