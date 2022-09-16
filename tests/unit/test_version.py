from rambler_google_activator.version import Version
from tests import *


class TestVersion(unittest.TestCase):
    def test_set_version(self):
        self.assertEqual(Version, Version)
