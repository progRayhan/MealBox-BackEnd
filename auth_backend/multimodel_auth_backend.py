from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from meal_user.models import Employee, Staff

class MultiModelAuthBackend(BaseBackend):
    req = None
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Try authenticating as a Customer
        self.req = request
        if request.POST.get('user_type')=='staff':
            try:
                user = Staff.objects.get(phone_number=username)
                if user and check_password(password, user.password):
                    return user
            except Staff.DoesNotExist:
                pass

        else:
            try:
                user = Employee.objects.get(phone_number=username)
                if user and check_password(password, user.password):
                    return user
            except Employee.DoesNotExist:
                pass

        return None

    def get_user(self, user_id):
        if self.req.POST.get('user_type') == 'employee':
            try:
                return Employee.objects.get(pk=user_id)
            except Employee.DoesNotExist:
                return None
        else:
            try:
                return Staff.objects.get(pk=user_id)
            except Staff.DoesNotExist:
                return None
