from django.urls import path
from webapp.views import search_users, IndexView, SubscriptionCreateView, SubscriptionDeleteView, LikeCreateView, \
    CommentView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('serch/', search_users, name='search'),
    path('user_profile/<int:pk>/subscribe/', SubscriptionCreateView.as_view(), name='subscribe'),
    path('user_profile/<int:pk>/unsubscribe/', SubscriptionDeleteView.as_view(), name='unsubscribe'),
    path('publication_like/<int:pk>/like/', LikeCreateView.as_view(), name='like'),
    path('comment/<int:pk>/', CommentView.as_view(), name='comment'),
    # path('post/<int:pk>/', DetailPost.as_view(), name='detail_post'),
]