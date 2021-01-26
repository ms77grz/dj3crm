from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class OrganisorAndLoginRequiredMixin(AccessMixin):
    """Verify that current user is an organisor and is authenticated"""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_organisor or not request.user.is_authenticated:
            return redirect('logout')
        return super().dispatch(request, *args, **kwargs)
