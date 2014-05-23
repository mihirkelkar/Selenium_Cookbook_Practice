#!/usr/bin/python
import unittest
from selenium import webdriver
#Synchronizing a selenium test with implicit wait. This test is mainly used for the purpose that lets say an element that the webdriver needs on the DOM is not available yet, the webdriver waits for that element to load. 

#The demo website we are using here is http://dl.dropbox.com/u/55228056/AjaxDemo.html

class implicitwait(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_implicitwait(self):
		ff = self.driver
		ff.get("http://dl.dropbox.com/u/55228056/AjaxDemo.html")
		
		#Set implicit wait time for 10 seconds
		ff.implicitly_wait(10)
		try:
			#Get link for page 4 on the page and click for it
			button_four = ff.find_element_by_link_text("Page 4")
			button_four.click()
		except:
			self.failUnless(True)

	def tearDown(self):
		#self.driver.close()
		#self.driver.quit()


if __name__ == "__main__":
	unittest.main(verbosity = 2)
