from django.contrib.auth.backends import ModelBackend
from .models import useracount

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = useracount.objects.get(email=email)
        except useracount.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        try:
            return useracount.objects.get(pk=user_id)
        except useracount.DoesNotExist:
            return None