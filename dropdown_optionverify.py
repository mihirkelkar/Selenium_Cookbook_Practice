#!/usr/bin/python
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class dropdown_textverification(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		
	def testverify_dropdowncontent(self):
		ff = self.driver
		ff.get("https://facebook.com")
		yearrange = ["year".title()] + [str(x) for x in range(1905, 2015)][::-1]
		#print yearrange
		year = Select(ff.find_element_by_name("birthday_year"))
		contents = [x.text.encode("utf-8") for x in year.options]
		self.assertEquals(yearrange, contents)

	def tearDown(self):
		self.driver.close()
		self.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)



