from selenium import webdriver
import unittest
"""This example looks to shoew the use of retreving text from elements that you have selected and then using the assertIn statement to see of a word is present in the given selected tags text"""
class Testcase(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
	
	def test_some_website(self):
		self.driver.get("http://saucelabs.com/test/guinea-pig")
		body = self.driver.find_element_by_tag_name("body")
		print body.text
	
	def tearDown(self):
		self.driver.close()
		self.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)
