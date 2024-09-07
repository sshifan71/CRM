from  django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.shortcuts import redirect

class OrganizorAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated or is an organizor."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organizor:
            return redirect("lead_list")
        return super().dispatch(request, *args, **kwargs)
