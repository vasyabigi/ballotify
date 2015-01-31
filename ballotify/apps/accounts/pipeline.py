from datetime import datetime
from .models import User


def create_user(strategy, details, response, user=None, *args, **kwargs):
    if user:
        return {'is_new': False}

    fields = {
        'email': details.get('email'),
        'username': details.get('username'),
        'name': details.get('fullname'),
        'gender': response.get('gender'),
        'birthday': datetime.strptime(response.get('birthday'), "%m/%d/%Y") if response.get('birthday') else None,
        'hometown': response.get('hometown'),
        'link': response.get('link'),
    }

    return {
        'is_new': True,
        'user': User.objects.create_user(**fields)
    }
