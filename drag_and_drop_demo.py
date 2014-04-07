"""This code demostrates how to pick p objects and drag them around in a webpage using some sweet python selenium tricks"""

from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
class draganddrop(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()
	
	def test_draganddrop(self):
		self.driver.get("http://dl.dropbox.com/u/55228056/DragDropDemo.html")
		dragsource = self.driver.find_element_by_xpath("//div[@id = 'draggable']")
		dragtarget = self.driver.find_element_by_xpath("//div[@id = 'droppable']")

		action_chains = ActionChains(self.driver)
		action_chains.drag_and_drop(dragsource, dragtarget)

	def tearDown(self):
		self.driver.close()
		self.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)
