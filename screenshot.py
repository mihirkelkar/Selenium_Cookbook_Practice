#!/usr/bin/python
from selenium import webdriver
import unittest

class capture_screen_shot(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_takeScreenshot(self):
		self.driver.get("https://www.google.com/")
		self.driver.save_screenshot("screenshot.png")
	
	def tearDown(self):
		self.driver.close()
		self.driver.quit() 


if __name__ == "__main__":
	unittest.main(verbosity = 2)
