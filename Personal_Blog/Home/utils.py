"""
    Project utils
"""

from django.shortcuts import redirect


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
