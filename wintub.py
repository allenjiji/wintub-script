import requests
from bs4 import BeautifulSoup
import pandas as pd
from prettytable import PrettyTable
url = 'https://s5.wintub.com/login.php'
dash_url = 'https://s5.wintub.com/dashboard.php'
count=0

fileToRead = './wintub-mails.txt'
file = open(fileToRead,'r')
listLine = file.readlines()
email_list = [obj.rstrip('\n') for obj in listLine]

print(email_list)

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
print("Press any key to CLOSE")
getch()
