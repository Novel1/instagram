from django.urls import path

from api.views import AccountSimpleView, CommentSimpleView, LikeSimpleView, SubscribeSimpleView, PostSimpleView

urlpatterns = [
    path('account/', AccountSimpleView.as_view(), name='account_view'),
    path('comment/', CommentSimpleView.as_view(), name='comment_view'),
    path('like/', LikeSimpleView.as_view(), name='like_view'),
    path('posts/', PostSimpleView.as_view(), name='post_view'),
    path('subcribe/', SubscribeSimpleView.as_view(), name='subscribe_view')
]