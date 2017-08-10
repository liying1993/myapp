import json
import os
import unittest
from io import StringIO
from pprint import pprint
from app import create_app


class TestApi(unittest.TestCase):
    def setUp(self):
        os.chdir("..")
        self.app = create_app().test_client()

    def request_get(self, uri, user_uid=None, user_token=None):
        print("GET {}".format(uri))
        headers = {"Content-Type": "application/json"}
        if user_uid and user_token:
            headers["UserID"] = user_uid,
            headers["AccessToken"] = user_token

        self.request = self.app.get(
            uri,
            headers=headers)
        print(self.request._status)
        print(self.request.headers)
        try:
            pprint(json.loads(self.request.data.decode("utf-8")))
        except json.JSONDecodeError:
            print("{}".format(self.request.data.decode("utf-8")))

    def request_post(self, uri, data, user_uid=None, user_token=None):
        print("POST {}".format(uri))
        headers = {"Content-Type": "application/json"}
        if user_uid and user_token:
            headers["UserID"] = user_uid,
            headers["AccessToken"] = user_token

        self.request = self.app.post(
            uri,
            headers=headers,
            input_stream=StringIO(json.dumps(data)))
        print(self.request._status)
        print(self.request.headers)
        try:
            pprint(json.loads(self.request.data.decode("utf-8")))
        except json.JSONDecodeError:
            print("{}".format(self.request.data.decode("utf-8")))

    def request_put(self, uri, data, user_uid=None, user_token=None):
        print("PUT {}".format(uri))
        headers = {"Content-Type": "application/json"}
        if user_uid and user_token:
            headers["UserID"] = user_uid,
            headers["AccessToken"] = user_token

        self.request = self.app.put(
            uri,
            headers=headers,
            input_stream=StringIO(json.dumps(data)))
        print(self.request._status)
        print(self.request.headers)
        try:
            pprint(json.loads(self.request.data.decode("utf-8")))
        except json.JSONDecodeError:
            print("{}".format(self.request.data.decode("utf-8")))

    def request_delete(self, uri, user_uid=None, user_token=None):
        print("DELETE {}".format(uri))
        headers = {"Content-Type": "application/json"}
        if user_uid and user_token:
            headers["UserID"] = user_uid,
            headers["AccessToken"] = user_token

        self.request = self.app.delete(
            uri,
            headers=headers)
        print(self.request._status)
        print(self.request.headers)
        try:
            pprint(json.loads(self.request.data.decode("utf-8")))
        except json.JSONDecodeError:
            print("{}".format(self.request.data.decode("utf-8")))

if __name__ == '__main__':
    unittest.main()
