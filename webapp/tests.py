from app import app
import unittest


class AppTestCase(unittest.TestCase):

    def test_root_text(self):
        tester = app.test_client(self)
        response = tester.get('/')
        assert 'Hello world!' in response.data

    def test_hostname_text(self):
        tester = app.test_client(self)
        response = tester.get('/hostname/')
        assert 'This is an example wsgi app served from' in response.data


if __name__ == '__main__':
    unittest.main()
