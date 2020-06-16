import requests
from bs4 import BeautifulSoup
import pandas as pd
from prettytable import PrettyTable
url = 'https://s6.wintub.com/login.php'
dash_url = 'https://s6.wintub.com/dashboard.php'
email_list = ['allunaduvilaveettil@gmail.com','newadmail1@gmail.com','newadmail2@gmail.com','newadmail3@gmail.com','newadmail4@gmail.com','newadmail5@gmail.com','newadmail6@gmail.com','newadmail7@gmail.com','newadmail8@gmail.com','newadmail9@gmail.com','newadmail10@gmail.com','newadmail11@gmail.com',]
for email in email_list:
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
          print("Iterated "+email)
    except:
        print("Operation Failed")
    print("Completed for k mail with God's Grace")

print("TASK COMPLETED WITH GOD'S GRACE!")
