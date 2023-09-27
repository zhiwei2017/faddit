from unittest import TestCase
from fastapi.testclient import TestClient
from feddit.app.application import create_application


class TestBaseEventHandler(TestCase):
    def test_startup_handler(self):
        app = create_application()
        with self.assertLogs('feddit', level='INFO') as cm:

            with TestClient(app):
                pass
            self.assertIn('INFO:feddit:Starting up ...', cm.output)
            self.assertIn('INFO:feddit:Shutting down ...', cm.output)
