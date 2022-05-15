import requests
from bs4 import BeautifulSoup
import time

def search_botanic():
    url = "https://smartstore.naver.com/julie_botanic/category/ALL?st=RECENT&free=false&dt=BIG_IMAGE&page=1&size=40"
    r = requests.get(url)
    bs = BeautifulSoup(r.content, "lxml")
    spans = bs.select("span.nIAdxeTzhx")

    for s in spans:
        price = s.text
    
        if price == "100":
            message_p()
            message_j()

import os
from twilio.rest import Client


def message_p():
    account_sid_p = 'AC4adcbbc5a0491b9e469f0fde21248fe6'
    auth_token_p = 'e9269acfbc8bbf36847b5280ce64ee1f'
    client = Client(account_sid_p, auth_token_p)

    message = client.messages \
                    .create(
                        body="!!100원 이벤트 등장등장!!",
                        from_='+19707030181',
                        to='+821048488489'
                    )

    print(message.sid)

def message_j():
    account_sid_j = 'AC2b4a32218a13a1441318328ae0d75a87'
    auth_token_j = '8fd33dbc6204f6733d9e2ea0d54c18eb'
    client = Client(account_sid_j, auth_token_j)

    message = client.messages \
                    .create(
                        body="!!100원 이벤트 등장등장!!",
                        from_='+19853317764',
                        to='+821029905275'
                    )

    print(message.sid)


while True:
    search_botanic()
    time.sleep(10)