import requests
from bs4 import BeautifulSoup
import pandas as pd
from prettytable import PrettyTable
url = 'https://s5.wintub.com/login.php'
dash_url = 'https://s5.wintub.com/dashboard.php'
count=0
#email_list = ['allunaduvilaveettil@gmail.com','newadmail1@gmail.com','newadmail2@gmail.com','newadmail3@gmail.com','newadmail4@gmail.com','newadmail5@gmail.com','newadmail6@gmail.com','newadmail7@gmail.com','newadmail8@gmail.com','newadmail9@gmail.com','newadmail10@gmail.com','newadmail11@gmail.com','newadmail12@gmail.com','newadmail13@gmail.com','newadmail14@gmail.com','newadmail15@gmail.com','newadmail16@gmail.com','newadmail17@gmail.com','newadmail18@gmail.com','newadmail19@gmail.com','newadmail20@gmail.com','newadmail21@gmail.com','newadmail22@gmail.com','newadmail23@gmail.com','newadmail24@gmail.com','newadmail25@gmail.com','newadmail26@gmail.com','newadmail27@gmail.com','newadmail28@gmail.com','newadmail29@gmail.com','newadmail30@gmail.com','newadmail31@gmail.com','newadmail32@gmail.com','newadmail33@gmail.com','newadmail34@gmail.com','newadmail35@gmail.com','newadmail36@gmail.com','newadmail37@gmail.com','newadmail38@gmail.com','newadmail39@gmail.com','santhoshsivan08072004@gmail.com','sureshkrishna16072003@gmail.com','ishanakrishna06072006@gmail.com','najeebarshad01072005@gmail.com','theresagregorious@gmail.com','thabithabenoy@gmail.com']


fileToRead = './demo.txt'
file = open(fileToRead,'r')
listLine = file.readlines()
email_list = [obj.rstrip('\n') for obj in listLine]



for email in email_list:
    count = count+1
    login_data = {'email':email,'password':'qwerty'}
    session =  requests.Session()
    page = session.post(url,login_data)
    print(page)
    main_page = session.get(dash_url)
    print(main_page)
    soup = BeautifulSoup(main_page.content,'html.parser')
    #print(soup)
    try:
        a = soup.find('a',{'id':'proceed'},attr = {})
        #print(a)
        #print(a['href'])
        appendable = a['href']
        a=appendable.split('&')
        for i in range(1,6):
          print(i)
          a[0]='?v='+str(i)+'&'
          b=a[0]+a[1]
          print(dash_url+b)
          task_page = session.get(dash_url+b)
          print(task_page)
          print(" Watched "+str(i)+" Video for "+email)
    except:
        print("Operation Failed")
    print("Completed for "+str(count)+ " mail with God's Grace")

print("TASK COMPLETED WITH GOD'S GRACE!")
