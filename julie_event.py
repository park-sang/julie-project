from pip import main
import requests
from bs4 import BeautifulSoup
import time
import os
import json
import os
from twilio.rest import Client


def kakao():
    with open("kakao_code.json","r") as fp:
        tokens = json.load(fp)
    url="https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers={
        "Authorization" : "Bearer " + tokens["access_token"]
    }
    data={
        "template_object": json.dumps({
            "object_type":"text",
            "text":"!!줄리보타닉 100원 이벤트!!" + "\n" + "링크 바로가기" + "\n" + "https://smartstore.naver.com/julie_botanic/category/ALL?st=RECENT&free=false&dt=BIG_IMAGE&page=1&size=40",
            "link":{
                "web_url":"www.naver.com"
            }
        })
    }

    response = requests.post(url, headers=headers, data=data)
    response.status_code


def search_botanic():
    url = "https://smartstore.naver.com/julie_botanic/category/ALL?st=RECENT&free=false&dt=BIG_IMAGE&page=1&size=40"
    r = requests.get(url)
    bs = BeautifulSoup(r.content, "lxml")
    spans = bs.select("span.nIAdxeTzhx")

    for s in spans:
        price = s.text
    
        if price == "100":
            kakao()     #나에게 카카오톡 메시지 보내기
            message_p() #나에게 문자 메시지 보내기
            message_j() #친구에게 문자 메시지 보내기
            


def message_p():
    account_sid_p = 'AC4adcbbc5a0491b9e469f0fde21248fe6'
    auth_token_p = 'e9269acfbc8bbf36847b5280ce64ee1f'
    client = Client(account_sid_p, auth_token_p)

    message = client.messages \
                    .create(
                        body="!!100원 이벤트 등장등장!!",
                        from_='+19707030181',
                        to='핸드폰 번호'
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
                        to='핸드폰 번호'
                    )

    print(message.sid)


while True:
    search_botanic()
    time.sleep(10)
