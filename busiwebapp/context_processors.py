# Context processors for providing global template context
from .models import UserProfile

def user_profile_context(request):
    """
    Adds user profile context to all templates
    """
    context = {}
    if request.user.is_authenticated:
        try:
            context['user_profile'] = request.user.userprofile
        except UserProfile.DoesNotExist:
            # Create UserProfile if it doesn't exist
            context['user_profile'] = UserProfile.objects.create(user=request.user)
    return context
