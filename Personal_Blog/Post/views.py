from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from .models import Post
from .forms import PostForm


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


class CreatePost(View):
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
