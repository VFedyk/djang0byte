from django.contrib.auth.models import User
from annoying.decorators import ajax_request

@ajax_request
def check(request, type, value, value_2 = None):
    if type == 'mail':
        try:
            User.objects.get(email=value)
            return {'value': False, 'type': type}
        except User.DoesNotExist:
            return {'value': True, 'type': type}
    elif type == 'username':
        try:
            User.objects.get(username=value)
            return {'value': False, 'type': type}
        except User.DoesNotExist:
            return {'value': True, 'type': type}
    elif type == 'all':
        try:
            User.objects.get(email=value_2)
            mail = False
        except User.DoesNotExist:
            mail = True
        try:
            User.objects.get(username=value)
            username = False
        except User.DoesNotExist:
            username = True
        return {'username': username, 'mail': mail}