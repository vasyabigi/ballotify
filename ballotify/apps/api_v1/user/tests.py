import json

from rest_framework import status

from core.tests import BaseTestCase


class UserTestCase(BaseTestCase):
    def setUp(self):
        self.user_details = "/v1/user/"
        super(UserTestCase, self).setUp()

    def test_retrieve_user_details_return_valid_user(self):
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
