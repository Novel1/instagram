from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, FormView
from posts.models import Post, Comment
from webapp.forms import CommentForm
from webapp.models import Subscription, Like


# Create your views here.


class IndexView(ListView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'posts'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['comment_form'] = CommentForm()
        return context


def search_users(request):
    query = request.GET.get('q')
    users = get_user_model().objects.filter(
        Q(username__iexact=query) |
        Q(first_name__iexact=query) |
        Q(email__iexact=query)
    )
    return render(request, 'search_results.html', {'users': users})


class SubscriptionCreateView(LoginRequiredMixin, CreateView):
    model = Subscription
    fields = []
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        subscribed_to = get_object_or_404(get_user_model(), pk=self.kwargs.get('pk'))
        subscription = form.save(commit=False)
        subscription.subscriber = self.request.user
        subscription.subscribed_to = subscribed_to
        subscription.save()
        subscribed_to.subscribers_count += 1
        subscribed_to.save()
        self.request.user.subscriptions_count += 1
        self.request.user.save()
        return super().form_valid(form)


class SubscriptionDeleteView(LoginRequiredMixin, DeleteView):
    model = Subscription
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        subscription = self.get_object()
        subscribed_to = subscription.subscribed_to
        subscribed_to.subscribers_count -= 1
        subscribed_to.save()
        self.request.user.subscriptions_count -= 1
        self.request.user.save()
        return super().form_valid(form)


class LikeCreateView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        post_id = kwargs['pk']
        post = Post.objects.get(id=post_id)
        try:
            like = Like.objects.get(post=post, user=request.user)
            like.delete()
            post.likes_count -= 1
        except Like.DoesNotExist:
            like = Like.objects.create(post=post, user=request.user)
            post.likes_count += 1
        post.save()
        return JsonResponse({'likes_count': post.likes_count})


class CommentView(LoginRequiredMixin, FormView):
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            author = request.user
            if not Comment.objects.filter(author=author, post=post).exists():
                Comment.objects.create(author=author, post=post, text=text)
        return redirect('index')

#
# class DetailPost(LoginRequiredMixin, DetailView):
#     model = Post
#     template_name = 'post_detail.html'
#     context_object_name = 'post'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         likes = self.object.likes.all()
#         context['post_like'] = likes.values_list('user_id', flat=True)
#         # context['form'] = CommentForm(instance=self.object)
#         return context