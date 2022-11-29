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
        fields = ('id', 'username',)


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    parent_post = PostSerializer()
    owner = PartInfoUserSerializer()
    # text = TextSerializer()

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):

        return Comment.objects.create(
            **validated_data,
            parent_post=Post.objects.get(id=validated_data['parent_post']),
            owner=UserModel.objects.get(id=validated_data['owner'])
        )