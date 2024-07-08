from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from .models import Profile

class CheckApprovalMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            if not request.user.is_superuser:
                try:
                    allowed_paths = [
                        reverse('user_auth:await_approval'),
                        reverse('user_auth:logout'),
                        reverse('user_auth:login'),
                        reverse('home:home')
                    ]
                    if not request.user.profile.is_approved and request.path not in allowed_paths:
                        return redirect('user_auth:await_approval')
                except Profile.DoesNotExist:
                    Profile.objects.create(user=request.user)  # Create profile if it doesn't exist
                    return redirect('user_auth:await_approval')
        return None
