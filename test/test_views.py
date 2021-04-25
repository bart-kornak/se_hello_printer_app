import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        self.assertEqual(b'{ "imie": "Bartek", "mgs": "Hello World!"}',
                         rv.data)

    def test_msg_with_output1(self):
        rv = self.app.get('/?output=xml')
        self.assertEqual(b"<greetings>\n\t<name>Bartek</name> \n\t<msg>Hello World!</msg> \n</greetings>\n", rv.data) # noqa
