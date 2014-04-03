"""Just a boiler plate example about how to connect to a website using the selenium webdriver
"""
from selenium import webdriver
import unittest

class Selenium_test(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_website(self):
		self.driver.get("http://saucelabs.com/test/guinea-pig")
		self.assertEqual("I am a page title - Sauce Labs", self.driver.title)
		#Assert Equal is basically fail if both entities are unequal

	def tearDown(self):
		self.driver.close()
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()
