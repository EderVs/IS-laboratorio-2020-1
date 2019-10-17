from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .utils import IsNotAuthenticatedMixin
from Post.models import Post
from .forms import LoginForm


# Function Views
def index(request):
    """
        Index in my Web Page.
    """
    print(request.method)
    template = 'Home/index.html'
    context = {}
    return render(request, template, context)


# Class-based Views
class Index(View):
    """
        Index in my Web Page but with Clased based views.
    """
    template = 'Home/index.html'
    context = {'title': 'Index'}

    def get(self, request):
        """
            Get in my Index.
        """
        all_posts = Post.objects.all()
        self.context['posts'] = all_posts
        return render(request, self.template, self.context)


class About(View):
    """
        About me page.
    """
    template = 'Home/about.html'
    context = {'title': 'About me'}

    def get(self, request):
        """
            Get in About me.
        """
        return render(request, self.template, self.context)


class Login(IsNotAuthenticatedMixin, View):
    """
        Admin login
    """
    template = 'Home/login.html'
    context = {'title': 'Admin Login'}

    def get(self, request):
        """
            Shows the form to login
        """
        form = LoginForm()
        self.context['form'] = form

        return render(request, self.template, self.context)

    def post(self, request):
        """
            Validates and do the login
        """
        form = LoginForm(request.POST)
        if form.is_valid():
            users = User.objects.filter(email=form.cleaned_data['email'])
            if len(users) > 0:
                user = authenticate(request, username=users[0].username, password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    if request.GET.get("next", None) is not None:
                        return redirect(request.GET.get("next"))
                    return redirect('Home:index')

        self.context['form'] = form
        return render(request, self.template, self.context)


class Logout(LoginRequiredMixin, View):
    """
        Does the logout
    """
    def get(self, request):
        logout(request)
        return redirect("Home:index")
