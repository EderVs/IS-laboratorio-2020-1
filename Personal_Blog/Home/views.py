from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .utils import IsNotAuthenticatedMixin, NotificationView
from .forms import LoginForm, SubscriberForm
from .models import Subscriber
from Post.models import Post


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
class Index(NotificationView):
    """
        Index in my Web Page but with Clased based views.
    """

    def __init__(self):
        super().__init__()
        self.template = 'Home/index.html'
        self.context['title'] = 'Index'

    def get(self, request):
        """
            Get in my Index.
        """
        all_posts = Post.objects.all()
        subscriber_form = SubscriberForm()

        # Notifications
        self.context['notification_message'] = request.GET.get('notification-message', '')
        self.context['notification_type'] = request.GET.get('notification-type', 'normal')

        self.context.update({
            'posts': all_posts,
            'subscriber_form': subscriber_form
        })
        return render(request, self.template, self.context)


class AddSubscriber(View):
    """
        Adding to the Newsletter
    """

    def post(self, request):
        subscriber_form = SubscriberForm(request.POST)
        if subscriber_form.is_valid():
            new_subscriber = Subscriber(
                email=subscriber_form.cleaned_data['email']
            )
            new_subscriber.save()

        return redirect('Home:index')


class About(View):
    """
        About me page.
    """

    def __init__(self):
        super().__init__()
        self.template = 'Home/about.html'
        self.context['title'] = 'About me'

    def get(self, request):
        """
            Get in About me.
        """
        return render(request, self.template, self.context)


class Login(IsNotAuthenticatedMixin, NotificationView):
    """
        Admin login
    """

    def __init__(self):
        super().__init__()
        self.template = 'Home/login.html'
        self.context['title'] = 'Admin Login'

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
                else:
                    form.add_error("password", "Password incorrect")
            else:
                form.add_error("email", "This email doesn't exist")

        self.context['form'] = form
        return render(request, self.template, self.context)


class Logout(LoginRequiredMixin, View):
    """
        Does the logout
    """
    def get(self, request):
        logout(request)
        return redirect("Home:index")
