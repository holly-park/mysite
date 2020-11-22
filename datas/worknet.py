from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import datetime
from selenium import webdriver
import time,os

# res = requests.get('http://media.daum.net/economic/')
# if res.status_code == 200:
#     soup = BeautifulSoup(res.content, 'html.parser')
#     links = soup.find_all('a', class_='link_txt')
#     print('task_crawling_daum : ', type(links), len(links))
#     dates = list()
#     title = str()
#     link = str()
#     for link in links:
#         title = str.strip(link.get_text())
#         link = link.get('href')
#         data = {"title": title, "link": link, "create_date": datetime.datetime.now()}
#         dates.append(data)

#     with MongoClient('mongodb://192.168.0.6:27017/')  as client:
#         mydb = client.mydb
#         res = mydb.economic.insert_many(dates)

path = "./datas/driver/chromedriver"
driver = webdriver.Chrome(executable_path=path)
driver.implicitly_wait(5)

def dataInput():
    url='https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?occupation=&_csrf=76266fe2-3137-427d-8f43-f7c1a6f45da5&region=&keyword=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
    driver.get(url=url)
    
    #data={'jobs':'', 'companies':'', 'date':''}
    # data[jobs]=''
    # data[companies]=''
    # data[date]=''
    job = driver.find_elements_by_class_name('cp-info-in')
    job_title = []
    for i in job:
        # print(i.text)
        job_title.append(i.text)
        #data[jobs].append(i.text)

    company = driver.find_elements_by_class_name('cp_name')
    company_name = []
    for name in company:
        #print(name.text)
        company_name.append(name.text)
        #data[companies].append(name.text)
    
    deadline= []
    for a in range(1,10):
        deadline = driver.find_element_by_id(f'dDayInfo{a}')
        #print(date.text)
        deadline.append(date.text)
        #data[date].append(deadline.text)

    data = {'jobs':job_title, 'companies': company_name, 'date':deadline}
    

    db_url = 'mongodb://192.168.219.138:27017/'
    
    with MongoClient(db_url) as client:
        sampledb = client['worknet']
        inserToDB = sampledb.samplecollection.insert_one(data)
    
    

dataInput()

        