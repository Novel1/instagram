from rest_framework import serializers

from accounts.models import Account
from posts.models import Post, Comment
from webapp.models import Like, Subscription


class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            '__all__'
        )


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            '__all__'
        )


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            '__all__'
        )


class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            '__all__'
        )


class SubscribeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = (
            '__all__'
        )
