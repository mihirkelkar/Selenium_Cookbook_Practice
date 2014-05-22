import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class selectdropdown(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()
	def test_dropdownmenu(self):
		ff = self.driver
		ff.get("https://facebook.com")
		#USING THE UTIL CALLED SELECT IS PRETTY SWEET
		month = Select(ff.find_element_by_name("birthday_month"))
		#SELECTING ALL OPTIONS FROM THE SELECT DROP DOWN MENU
		#print month.options
		try:
			month.select_all()

		except:
			pass
		self.assertEqual(13, len(month.options))
		day = Select(ff.find_element_by_name("birthday_day"))
		self.assertEqual(32, len(day.options))
		year = Select(ff.find_element_by_name("birthday_year"))
		self.assertEqual(111, len(year.options))

	def tearDown(self):
		self.driver.close()
		self.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)


