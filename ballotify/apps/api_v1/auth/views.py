from rest_framework import response
from rest_framework import serializers
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_jwt.settings import api_settings

from social.apps.django_app.utils import psa


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginView(ObtainJSONWebToken):
    """
    API View that receives a POST with a Facebook access token.
    Returns a JSON Web Token that can be used for authenticated requests.

    """
    def post(self, request):
        user = login_social_user(request, 'facebook')

        if user:
            payload = jwt_payload_handler(user)
            return response.Response({'token': jwt_encode_handler(payload)})
        else:
            raise serializers.ValidationError({
                api_settings.NON_FIELD_ERRORS_KEY: ['Unable to login with provided credentials.']
            })

login_view = LoginView.as_view()


@psa()
def login_social_user(request, backend):
    try:
        return request.backend.do_auth(request.DATA.get('token'), ajax=True)
    except Exception:
        pass
