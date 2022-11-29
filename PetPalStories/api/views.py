from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

from PetPalStories.api.serializers import CommentSerializer, PartInfoUserSerializer, PostSerializer
from PetPalStories.forum.models import Comment, Post
from rest_framework import generics as rest_views, status

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
        data = request.data
        print(request.data)
        owner = UserModel.objects.get(id=request.data['owner'])
        data['owner'] = {"id": owner.id, "username": owner.username}
        post = Post.objects.get(id=request.data['parent_post'])
        # data['text'] = {'text': data['text']}
        data['parent_post'] = {"id": post.id, "owner": post.owner.pk, "topic": post.topic}
        # new_comment = CommentSerializer(data=data)
        # if new_comment.is_valid():
        #     new_comment.save()
        new_comment = Comment.objects.create(text=data['text'], owner=owner, parent_post=post)
        new_comment.save()

        return super().post(request, *args, **kwargs)