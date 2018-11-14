import backports.unittest_mock
backports.unittest_mock.install()
from ansible_tower.job_template import Client
from ansible_tower.job_template import JobTemplate
import unittest
from unittest.mock import patch

class MyTest(unittest.TestCase):
    def test(self):
        client = Client("https://nu.nl", "ik", "geheim")
        jt = JobTemplate(client, "job", "project", "template")
        self.assertEqual(client.username, "ik")
        self.assertEqual(jt.get_resource(), "{ jobtemplate: 10 }")

    @patch('ansible_tower.job_template.Client.get_resource_id')
    def test_mock(self, mock_resource_id):
        mock_resource_id.return_value = 11
        client = Client("https://nu.nl", "ik", "geheim")
        jt = JobTemplate(client, "job", "project", "template")
        self.assertEqual(client.username, "ik")
        self.assertEqual(jt.get_resource(), "{ jobtemplate: 11 }")
        mock_resource_id.assert_called()
        mock_resource_id.assert_called_once_with('job')


if __name__ == '__main__':
    unittest.main()
