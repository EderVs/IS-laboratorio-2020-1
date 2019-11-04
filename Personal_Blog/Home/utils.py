"""
    Project utils
"""

from django.shortcuts import redirect
from django.views.generic.base import ContextMixin
from django.views import View


class IsNotAuthenticatedMixin:
    """
        Returns to the index if the user is authenticated
    """
    redirect_url = "Home:index"

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect(self.redirect_url)


class NotificationView(ContextMixin, View):
    """
        Adds notifications to the view's context
    """

    def __init__(self):
        self.context = super().get_context_data()
        self.context['notification_message'] = ""
        self.context['notification_type'] = ""