import unittest
from flaskhome import app

class testHello(unittest.TestCase):
	def setUp(self):
		app.testing = True
		self.app = app.test_client()
	def test_hello(self):
		rv = self.app.get("/")
		#self.assertEqual(rv.status, "200 OK")
		self.assertEqual(rv.data, b'hello world')

if __name__ == '__main__':
	unittest.main()
