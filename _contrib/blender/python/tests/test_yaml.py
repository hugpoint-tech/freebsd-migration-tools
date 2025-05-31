import tempfile
import unittest

import yaml

from phab_tool import common


class YamlTest(unittest.TestCase):
    def test_string_quoting(self):

        data = {
            "actual_int": 47,
            "leading_zero": "047",
            "valid_int": "47",
        }

        with tempfile.NamedTemporaryFile() as testfile:
            common.saveYamlFile(data, testfile.name)

            testfile.seek(0)
            ondisk: bytes = testfile.read()

            testfile.seek(0)
            loaded = yaml.load(testfile, yaml.Loader)

        self.assertEqual(data, loaded)
        self.assertEqual(
            b'"actual_int": 47\n"leading_zero": "047"\n"valid_int": "47"\n', ondisk
        )
