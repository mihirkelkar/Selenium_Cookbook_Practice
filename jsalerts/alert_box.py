#This selenium webdriver code handles simple javascript alert boxes
import unittest
from selenium import webdriver

class jsalert(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
	def test_jsalert(self):
		ff = self.driver
		ff.get("file:///home/thinkpad/code/selenium/jsalerts/simplealert.html")
		#click the button on the page
		button = ff.find_element_by_tag_name("button")
		button.click()
		try:
			alert = ff.switch_to_alert()
			alert.accept()
		except:
			print "No such alert"
			self.driver.close()
			self.driver.quit()

	def tearDown(self):
		self.driver.close()
		self.driver.quit()
	
if __name__ == "__main__":
	unittest.main(verbosity = 2)
