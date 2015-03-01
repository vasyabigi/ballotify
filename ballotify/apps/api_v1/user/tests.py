import json

from rest_framework import status
from rest_framework.test import APIClient

from accounts.models import User
from core.tests import BaseTestCase
from streams.factories import StreamFactory


class UserTestCase(BaseTestCase):
    def setUp(self):
        super(UserTestCase, self).setUp()

        StreamFactory(owner=self.user)

        self.user_details = "/v1/user/"
        self.strems_list = "/v1/user/streams/"

    def test_retrieve_user_details_without_auth_header_return_401(self):
        client = APIClient()
        response = client.get(self.user_details)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response_json = json.loads(response.content)

        # Check response:
        self.assertEqual(response_json, {u'detail': u'Authentication credentials were not provided.'})

    def test_get_user_details_return_valid_user(self):
        response = self.client.get(self.user_details)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json = json.loads(response.content)

        # Check response:
        self.assertDictContainsSubset({
            u'username': u'pedro',
            u'name': u'John Doe',
            u'gender': u'male',
            u'email': u'john1@example.com'
        }, response_json)

        # Check db:
        self.assertEqual(self.user.username, "pedro")
        self.assertEqual(self.user.name, "John Doe")
        self.assertEqual(self.user.gender, "male")
        self.assertEqual(self.user.email, "john1@example.com")

    def test_update_user_details_return_updated_user(self):
        data = {
            "name": "Rambo 4"
        }

        response = self.client.patch(self.user_details, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json = json.loads(response.content)

        # Check response:
        self.assertDictContainsSubset({
            u'username': u'pedro',
            u'name': u'Rambo 4',
            u'gender': u'male'
        }, response_json)

        # Check db:
        user = User.objects.get(username="pedro")
        self.assertEqual(user.name, "Rambo 4")

    def test_get_user_streams_return_valid_streams_list(self):
        response = self.client.get(self.strems_list)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json = json.loads(response.content)

        # Check response:
        self.assertDictContainsSubset({
            u'slug': u'dont-stop-belivin',
            u'title': u"Don't stop believin'"
        }, response_json["results"][0])

        # Check db:
        self.assertEqual(self.user.owned_streams.count(), 1)

        stream = self.user.owned_streams.first()
        self.assertEqual(stream.slug, 'dont-stop-belivin')
        self.assertEqual(stream.title, "Don't stop believin'")
