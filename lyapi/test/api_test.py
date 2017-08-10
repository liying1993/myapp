from test.api import TestApi

class Test(TestApi):
    def test(self):
        # self.request_get('/login')

        self.request_post('/register', data={"telephone":"1236532565","password":"123456"})