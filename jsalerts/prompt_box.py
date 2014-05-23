#This code here deals with javascript boxes which prompt you type something in them

import unittest
from selenium import webdriver

class prompt_box(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
	def test_promptbox(self):
		ff = self.driver
		ff.get("file:///home/thinkpad/code/selenium/jsalerts/promptboxalert.html")
		ff.find_element_by_tag_name("button").click()
		try:
			alert = ff.switch_to_alert()
			#Fill in the prompt box
			alert.send_keys("Frank Underwood")
			#Click okay
			alert.accept()
		except:
			print "No such alert found"


if __name__ == "__main__":
	unittest.main(verbosity = 2)


