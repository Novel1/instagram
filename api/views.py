from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Account
from api.serializers import AccountSerializers, LikeSerializers, SubscribeSerializers, CommentSerializers, \
    PostSerializers
from posts.models import Comment, Post
from webapp.models import Like, Subscription


class AccountSimpleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        account = Account.objects.all()
        serializer = AccountSerializers(account, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'gender': request.data.get('gender'),
            'inform': request.data.get('inform'),
            'phone': request.data.get('phone'),
            'language': request.data.get('language'),
            'email': request.data.get('email'),
            'avatar': request.data.get('avatar')
        }
        serializer = AccountSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeSimpleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        account = Like.objects.all()
        serializer = LikeSerializers(account, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'user': request.data.get('user'),
            'post': request.data.get('post')
        }
        serializer = LikeSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubscribeSimpleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        account = Subscription.objects.all()
        serializer = SubscribeSerializers(account, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'subscriber': request.data.get('subscriber'),
            'subscribed_to': request.data.get('subscribed_to')
        }
        serializer = SubscribeSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentSimpleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        account = Comment.objects.all()
        serializer = CommentSerializers(account, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'post': request.data.get('post'),
            'text': request.data.get('text'),
            'author': request.data.get('author'),
        }
        serializer = CommentSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostSimpleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        account = Post.objects.all()
        serializer = PostSerializers(account, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'descriptions': request.data.get('descriptions'),
            'image': request.data.get('image'),
            'author': request.data.get('author')
        }
        serializer = PostSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

