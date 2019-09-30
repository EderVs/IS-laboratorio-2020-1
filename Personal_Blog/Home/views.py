from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from Post.models import Post
from Home.forms import LoginForm


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


class Login(View):
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
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                if request.GET.get("next", None) is not None:
                    return redirect(request.GET.get("next"))
                return redirect('Home:index')

        self.context['form'] = form
        return render(request, self.template, self.context)


class Logout(View):
    """
        Does the logout
    """
    def get(self, request):
        logout(request)
        return redirect("Home:index")
