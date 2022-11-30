from django.contrib.auth import get_user_model

from PetPalStories.api.serializers import CommentSerializer
from PetPalStories.forum.models import Comment
from rest_framework import generics as rest_views

UserModel = get_user_model()


class CommentsListApiView(rest_views.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, *args, **kwargs):
        self.get_queryset()
        return super().get(*args, **kwargs)

    # def post(self, *args, **kwargs):
    #     return super().post(*args, **kwargs)

    def get_queryset(self):
        parent_post_id = self.request.query_params.get('query')
        queryset = self.queryset

        if parent_post_id:
            queryset = queryset.filter(parent_post_id=parent_post_id)

        return queryset.all().order_by('-published_on')


class CommentCreateView(rest_views.ListCreateAPIView):
    serializer_class = CommentSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)