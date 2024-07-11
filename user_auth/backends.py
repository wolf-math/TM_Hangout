from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class CaseInsensitiveModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(User.USERNAME_FIELD)
        try:
            case_insensitive_username_field = '{}__iexact'.format(User.USERNAME_FIELD)
            user = User._default_manager.get(**{case_insensitive_username_field: username})
        except User.DoesNotExist:
            User().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user