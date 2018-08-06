
import requests
import json

class AuthTest:
    def __init__(self, url):
        self.base_url = url
        self.endpoints = {
            "login": "/api/auth/login"
        }
        self.login = "hello@world.com"
        self.password = "12345678"
        
    def login_fail():
        login_url = self.base_url + self.endpoints['login']
        data = json.dumps(
            {
                'login': self.login,
                'password': self.password
            }
        )
        expected_data = {
            "success": false,
            "errors": {
                "email": [""],
                "password": [ ""],
                "message": "The password and email you entered don't match. If you forgot your password, use \"Forgot Password\""
            }
        }
        r = requests.post(login_url, data=data)
        actual_data = json.loads(r.text)
        assert actual_data == expected_data, "Login fail error expected. Got %s" % actual_data

def runTests():
    auth_test = new AuthTest(url='http://instatestvx.me')
    auth_test.login_fail()
