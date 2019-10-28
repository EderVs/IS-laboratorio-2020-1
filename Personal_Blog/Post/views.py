from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from .forms import PostForm
from .models import Post
from .utils import send_email


class OnePost(View):
    """
        Displays just one post
    """
    template = 'Post/one_post.html'
    context = {}

    def get(self, request, post_id):
        """
            GET in one post
        """
        # post = Post.objects.get(id=post_id)
        post = get_object_or_404(Post, id=post_id)
        self.context['post'] = post

        self.context['title'] = str(post)

        return render(request, self.template, self.context)


class CreatePost(LoginRequiredMixin, View):
    """
        Creates a new post
    """
    template = 'Post/create_post.html'
    context = {'title': 'Create a new post'}

    def get(self, request):
        """
            Shows the form to create a new post
        """
        form = PostForm()
        self.context['form'] = form

        return render(request, self.template, self.context)

    def post(self, request):
        """
            Validates and creates a new post
        """
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = Post(
                title = form.cleaned_data['title'],
                paragraph = form.cleaned_data['paragraph'],
                image = form.cleaned_data['image'],
            )
            new_post.save()

            # Sending email
            subject = 'There is a new Post here'
            content = 'New post: ' + new_post.title
            # Sending email to the same host
            send_email([settings.EMAIL_HOST_USER], subject, content)
            return redirect('Post:post_created')

        self.context['form'] = form
        return render(request, self.template, self.context)


class PostCreated(View):
    """
        Displays When a post is created
    """
    template = 'Post/post_created.html'
    context = {'title': 'Your post has been created!'}

    def get(self, request):
        """
            GET in post created
        """
        return render(request, self.template, self.context)
