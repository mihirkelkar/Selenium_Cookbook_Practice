import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

#SEE WHICH OPTION IS SELECTED AS DEFAULT IN THE DROP DOWN MENU
#HERE ALSO I WILL BE USING FACEBBOKS MAIN PAGE AS THE TESTING THINGY

class findselectedindropdown(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()
	def test_lookfordefaultselectedelement(self):
		ff = self.driver
		self.driver.get("https://facebook.com")
		month  = Select(ff.find_element_by_name("birthday_month"))
		option = month.first_selected_option
		print option.text

	def tearDown(self):
		self.driver.close()
		self.driver.quit()


if __name__ == "__main__":
	unittest.main(verbosity = 2)


