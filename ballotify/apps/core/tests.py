from rest_framework.test import APITestCase

from accounts.factories import UserFactory
from api_v1.auth.views import jwt_payload_handler, jwt_encode_handler


class APIv1TokenTestMixin(object):
    def get_token(self, user):
        self.client.force_authenticate(user)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return "JWT {}".format(token)


class BaseTestCase(APIv1TokenTestMixin, APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.user))
        super(BaseTestCase, self).setUp()
