import boto3
import os
from datetime import datetime
#from urllib.request import urlopen
import urllib.request as urllib2
import re

sns = boto3.client('sns')








def send_text(stock,price):
    sns.publish(
        Message=(
            'The price of {0} stock is {1}'.format(
                stock,
                price
            )
        ), 
        PhoneNumber='+16085351994'
    )



def lambda_handler(event, context):
    print('Getting stock')

    getStock()



def getStock():
    stockList=['TSLA','NET','FSLY','ATVI']

    stockListLength=len(stockList)
    
    
    i=0
    while i<stockListLength:
        stock=stockList[i]
        URL=URLString(stock)
        parser(stock,URL)
        i=i+1





def URLString(stock):
    URL='https://www.cnbc.com/quotes/?symbol='+stock
    return URL





def parser(stock,URL):
    user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
     
    headers = { 'User-Agent' : user_agent }


    req = urllib2.Request(URL, None, headers)


    response = urllib2.urlopen(req)
    
    page = response.read()
    response.close()


    page=str(page)
    
    splitText=page.split(",")

    
    k=28

    while k<30:
        #print(k)
        if "last" in splitText[k]:
            #print(k,splitText[k])
            lastString=splitText[k]
            price=re.findall("\d+\.\d+",lastString)
            send_text(stock,price)
            
        k=k+1