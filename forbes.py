from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import time
import datetime
driver = webdriver.Chrome()
#csv_file = open('forbeslist.csv', 'w')
# writer = csv.writer(csv_file)
# writer.writerow(['school', 'url'])

csv_file = open('forbesinfo.csv', 'w')
writer = csv.writer(csv_file)
writer.writerow(sorted(['school','student_population', 'undergrad_population', 'sf_ratio', 'total_cost','in_state_tuition','out_state_tuition',
	'percent_fin_aid', 'percent_admitted', 'SAT', 'ACT','rank']))
info_dict = {}

#driver.get("https://www.forbes.com/top-colleges/list/#tab:rank")
driver.get("https://www.forbes.com/top-colleges/list/3/#tab:rank")
time.sleep(4)
driver.find_element_by_xpath('//*[@class="continue-button"]').click()


#rows=driver.find_elements_by_xpath('//*[@id="list-table-body"]/tr[@class="data"]/td')
rows=driver.find_elements_by_xpath('//*[@id="list-table-body"]/tr[@class="data"]')
url = []
for row in rows:
	school_dict = {}
	name = row.find_element_by_xpath('./td[@class="name"]').text
	#school_dict['name']=name
	url.append(row.find_element_by_xpath('./td[@class="name"]/a').get_attribute("href"))
	#writer.writerow(school_dict.values())



print(url)

for i in range(0,len(url)):
	driver.get(url[i])
	info=driver.find_element_by_xpath('//*[@class="profileRight fright"]').text.split('\n')
	print(len(info))
	info_dict['school']=info[0]
	print (info[0])
	for j in range(1,len(info)):
		if info[j].find('Student Population')>=0:
			info_dict['student_population'] = info[j].split(": ")[1]
		elif info[j].find('Undergraduate Population')>=0:
			info_dict['undergrad_population'] = info[j].split(": ")[1]
		elif info[j].find('Student to Faculty')>=0:
			info_dict['sf_ratio'] = info[j].split(": ")[1]
		elif info[j].find('Total Annual Cost')>=0:
			info_dict['total_cost'] = info[j].split(": ")[1]
		elif info[j].find('In-State Tuition')>=0:
			info_dict['in_state_tuition'] = info[j].split(": ")[1]
		elif info[j].find('Out-of-State')>=0:
			info_dict['out_state_tuition'] = info[j].split(": ")[1]
		elif info[j].find('Percent on Financial Aid')>=0:
			info_dict['percent_fin_aid'] = info[j].split(": ")[1]
		elif info[j].find('Percent Admitted')>=0:
			info_dict['percent_admitted'] = info[j].split(": ")[1]
		elif info[j].find('SAT Composite')>=0:
			info_dict['SAT'] = info[j].split(": ")[1]
		elif info[j].find('ACT Composite')>=0:
			info_dict['ACT'] = info[j].split(": ")[1]
		elif info[j].find('Top Colleges')>=0:
			info_dict['rank'] = info[j].split(" ")[0]




			# info_dict['population']=info[2]
			# info_dict['sf_ratio']=info[4]
			# info_dict['total_cost']=info[5]
			# info_dict['in_state_tuition']=info[6]
			# info_dict['out_state_tuition']=info[7]
			# info_dict['percent_fin_aid']=info[8]
			# info_dict['avg_grant_aid']=info[9]
			# info_dict['percent_admitted']=info[10]
			# info_dict['SAT']=info[11]
			# info_dict['ACT']=info[12]
	keys_sorted = sorted(info_dict.keys())
	values_sorted = [info_dict[key] for key in keys_sorted]
	writer.writerow(values_sorted)


csv_file.close()

