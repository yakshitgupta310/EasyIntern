from bs4 import BeautifulSoup
import requests
import csv 

source=requests.get("https://internshala.com/internships/work-from-home-data%20science-jobs")
soup=BeautifulSoup(source.content,"lxml")

csv_file=open("jobs.csv","w")
csv_writer=csv.writer(csv_file)
csv_writer.writerow(["title","Company","location","duration","start Date","link"])

data=soup.find_all("div",class_="container-fluid individual_internship")

for x in data:
    title=x.find("div",class_="heading_4_5 profile").text
    company=x.find("div",class_="heading_6 company_name").text
    location=x.find("span").text
    duration=x.find_all("div",class_="item_body")
    details=x.find("a",class_="view_detail_button").get("href")
    detail="https://internshala.com"+details
    print(title)
    print(company)
    print(location)
    i=1
    for y in duration :
        if i==2:
            time=y.text
            print(time)
        if i==4 :
            start_date=y.text
            print(start_date)

        i+=1
    print(detail)
    csv_writer.writerow([title,company,location,time,start_date,detail])
        
  