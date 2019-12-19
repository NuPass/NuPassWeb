"""
    tests.NPWTestCase
    ~~~~~~~~~~~~~~~~~

    A test of NuPassWeb.

    :copyright: (c) 2019 by Sean Callaway.
    :license: GNU GPL v2, see LICENSE for more details.
"""
import unittest
from flask import json
from nupassweb import app


class NPWTestCase(unittest.TestCase):
    """Class for the testing of NuPassWeb."""

    def setUp(self):
        """Setup test client."""
        self.tester = app.test_client(self)

    def test_index(self):
        """Tests the index page."""
        response = self.tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_gen_pass_short(self):
        """Tests the gen_pass view for proper JSON on normal quantity."""
        response = self.tester.get('/gen_pass', query_string={'qty': '5'})
        data = json.loads(response.data)
        self.assertEqual(data["notice_str"], "")
        self.assertEqual(len(data["passwords"]), 5)
        self.assertEqual(data["rows"], 5)

    def test_gen_pass_long(self):
        """Tests the gen_pass view for proper JSON on oversized quantity."""
        response = self.tester.get('/gen_pass', query_string={'qty': '45'})
        data = json.loads(response.data)
        self.assertEqual(data["notice_str"],
                         "If more than 20 passwords are required, please " +
                         "rerun the tool or consider using the command-line " +
                         "version.\n\n")
        self.assertEqual(len(data["passwords"]), 20)
        self.assertEqual(data["rows"], 22)

    def test_404_page(self):
        """Verify we get a 404 error on a garbage path."""
        response = self.tester.get('/bad_path789456')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
