from selenium import webdriver
import unittest

class maximize_window_class(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
	
	def test_maximize_window(self):
		self.driver.get("https://www.nutanix.com")
		self.driver.maximize_window()

	def tearDown(self):
		self.driver.close()
		self.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)

