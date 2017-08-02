from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import time
import datetime

chop = webdriver.ChromeOptions()
chop.add_extension('Adblock-Plus_v.crx')
driver = webdriver.Chrome(chrome_options = chop)

csv_file = open('getschools.csv', 'w')
writer = csv.writer(csv_file)
writer.writerow(['forbes', 'ratemyprofessors','url'])

with open('forbeslist.csv', 'r') as f:
    reader = csv.reader(f)
    school_list = list(reader)
    print(school_list)

#school_list = ["harvard", "princeton"]
url_list=[]

for i in range(1,len(school_list)):
	get_dict={}
	try:
		driver.get("http://www.ratemyprofessors.com/search.jsp?queryBy=schoolName&query="+school_list[i][0])
		get_dict['forbes']=school_list[i][0]
		try:
			close = driver.find_element_by_link_text('Close')
			close.click()
			print('succesful close cookies window')
		except:
			pass
		try:
			result = driver.find_element_by_xpath('//li[@class="listing SCHOOL"]/a[1]')
			url = result.get_attribute("href")
			print(result.text)
			get_dict['ratemyprofessors']=result.text
			get_dict['url']=url
			writer.writerow(get_dict.values())
			url_list.append(url)
		except:
			print('couldnt find result:', school_list[i])
	except:
		print('you tried')
print(url_list)
csv_file.close()
#driver.get(url_list[0])


#FIXXXX