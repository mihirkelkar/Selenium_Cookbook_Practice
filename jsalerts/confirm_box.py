#In this code, we will deal with confirm boxes and confirm java script alerts

import unittest
from selenium import webdriver

class confirmalert(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()
	#Accepting a two button alert
	def test_confirmalert(self):
		ff = self.driver
		ff.get("file:///home/thinkpad/code/selenium/jsalerts/confirmboxalert.html")
		button = ff.find_element_by_tag_name("button")
		button.click()
		try:
			alert = ff.switch_to_alert()
			alert.accept()
		except:
			print "no such alert found"

	#Dismiss the test by clicking the cancel button on a two button alert
	def test_dismissalert(self):
		ff = self.driver
		ff.get("file:///home/thinkpad/code/selenium/jsalerts/confirmboxalert.html")
		button = ff.find_element_by_tag_name("button")
		button.click()
		try:
			alert = ff.switch_to_alert()
			alert.dismiss()
		except:
			print "no such alert found"
	def tearDown(self):
		self.driver.close()
		self.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)


