#Dealing with popup windows that appear when you click buttons using pytohn selenium.
import unittest
from selenium import webdriver

class popup(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
	def test_popup(self):
		ff = self.driver
		ff.get("file:///home/thinkpad/code/selenium/popup/popup.html")
		#The ff.window_handles will give you all the window handles within a session. indexed from 0  to n as per the time of creation of that window
		#Lets get the window handle of the cuurent session
		parent_window = ff.window_handles[0]
		#Finding the helpbutton on the popup.html page
		help_button = ff.find_element_by_id("helpbutton")
		#Clicking the help button would open a new popup window
		help_button.click()
		ff.switch_to_window(ff.window_handles[1])
		self.assertEquals(ff.title, "Cupertino")
		#Close the popup window
		ff.close()
		#Switch back to parent window
		ff.switch_to_window(parent_window)
		#Check if parent window is correct
		self.assertEquals(ff.title, "Good Morning America")
	def tearDown(self):
		self.driver.close()
		self.driver.quit()


if __name__ == "__main__":
	unittest.main(verbosity = 2)
