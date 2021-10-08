from  main import app
import  unittest
from fastapi.testclient import TestClient


class FastApiTest(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def tearDown(self) -> None:
        self.client = None

    def test_read_main(self):
        response = self.client.get("/items/items/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_read_one(self):
        response = self.client.get("/items/items/?limit=1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_websocket(self):
        with self.client.websocket_connect("/ws?token=" + "leizishuoceshi") as websocket:
            websocket.send_text("Hello WebSocket")
            data = websocket.receive_text()
            print(data)
            assert str(data) == "消息是: Hello WebSocket"

    def test_websocket_two(self):
        with self.client.websocket_connect("/ws?token=" + "leizishuoceshi") as websocket:
            websocket.send_text("Hello 123")
            data = websocket.receive_text()
            print(data)
            assert str(data) == "消息是: Hello 123"

if __name__ == "__main__":
    unittest.main()