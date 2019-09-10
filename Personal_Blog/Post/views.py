from django.shortcuts import get_object_or_404, render
from django.views import View

from .models import Post


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
