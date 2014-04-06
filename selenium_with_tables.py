"""Here we will read all the values present in the html table on the 676 HW 4 website making use of selenium. The objective is to use selenium to read tabl info and validate the correctness of the table"""

from selenium import webdriver
import unittest

class testtables(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()
	
	def test_tables(self):
		self.driver.get("http://www.csee.umbc.edu/~nicholas/676/term%20project/hw3.html")
		#Get all the rows that are present in this given table
		row_tags = self.driver.find_elements_by_css_selector("table[width = '458']>tbody>tr")
		#Make sure that the number of rows is 4
		self.assertEqual(len(row_tags), 4)
		#Iterate through every row which is present
		for i in row_tags:
			#For each row, find the column element and get its text.
			stuff = i.find_elements_by_css_selector("td")
			for j in stuff:
			#Some td element has an internal div element, however, the .text will bypass that and get the text which is present even inside the div and print it.
				print j.text

	def tearDown(self):
		self.driver.close()
		self.driver.quit()
	
if __name__ == "__main__":
	unittest.main(verbosity = 2)

