
import unittest
from selenium import webdriver

#Go to facebooks regestritation page and check the drag and drop menu for regs
#birthday and all,inline comments provide ample explanation 
class listmenutest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_dropmenu(self):
		ff  = self.driver
		ff.get("https:facebook.com")
		#Select the drop down menu which signifies month in the registration page
		month = ff.find_element_by_name("birthday_month")
		day = ff.find_element_by_name("birthday_day")
		year = ff.find_element_by_name("birthday_year")
		#Assert that the month has 12 entries in it
		self.assertEqual(13, len(month.find_elements_by_tag_name("option")))
		self.assertEqual(32, len(day.find_elements_by_tag_name("option")))
		self.assertEqual(111, len(year.find_elements_by_tag_name("option")))
		print "All assertions okay"
	def tearDown(self):
		self.driver.close()
		self.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)

