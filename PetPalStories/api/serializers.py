from django.contrib.auth import get_user_model
from rest_framework import serializers

from PetPalStories.forum.models import Post, Comment

UserModel = get_user_model()


#
# class TextSerializer(serializers.Serializer):
#     text = serializers.CharField()


class PartInfoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id',)


class CommentSerializer(serializers.ModelSerializer):
    parent_post = PostSerializer()
    owner = PartInfoUserSerializer()

    # text = TextSerializer()

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        parent_post = validated_data.pop('parent_post')

        owner = validated_data.pop('owner')

        return Comment.objects.create(text=validated_data['text'],
                                      parent_post=Post.objects.get(id=self._kwargs['data']['parent_post']['id']),
                                      owner=UserModel.objects.get(id=self._kwargs['data']['owner']['id']))