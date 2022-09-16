from datetime import date
from rambler_google_activator import RamblerEmail
from tests import *

class TestExample(unittest.TestCase):
    def test_email(self):
        email =  RamblerEmail("example@rambler.ru", "xxxxxxxxx")
        (status, code) = email.get_code(2)
        self.assertEqual(status, False)

    @pytest.mark.xfail
    def test_should_fail(self):
        self.assertEqual(False, True)
