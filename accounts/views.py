from django.contrib import messages
from django.contrib.auth import authenticate, logout, login, get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView

from accounts.forms import LoginForm, PostForm, UserChangeForm

from accounts.forms import CustomUserCreateForm
from posts.models import Post
from webapp.models import Subscription


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')
        username = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            messages.error(request, 'Пользователь не найден')
            return redirect('login')
        messages.success(request, 'Добро пожаловать!')
        login(request, user)
        return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')


class RegistrationView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreateForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        else:
            print(form.errors)
        context = {'form': form}
        return self.render_to_response(context)


class CretePost(CreateView):
    model = Post
    template_name = 'crete_post.html'
    form_class = PostForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            form.save()
            return redirect('/')
        context = {'form': form}
        return self.render_to_response(context)


class ProfileView(DetailView, PermissionRequiredMixin):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    permission_required = 'accounts.user_change'
    permission_denied_message = 'У вас не хватает прав доступа'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = self.object.posts.all()
        subscription = Subscription.objects.filter(subscriber=self.request.user, subscribed_to=user).first()
        context['subscription'] = subscription
        return context


class UserChangeView(UpdateView, PermissionRequiredMixin):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'

    # def get_queryset(self):
    #     return Post.objects.prefetch_related('comments')

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})

