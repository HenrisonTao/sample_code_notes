import requests
import time
import threading

cookies_hytao = {
    'serviceToken': 'XXXX',
    'xm_user_tw_num': '0',
    'guserid': 'XXX',
}

headers_hytao = {
    'authority': 'hd.c.mi.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'ser09',
    'origin': 'https://event.mi.com',
    'referer': 'X-2022',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

data = {
    'tag': 'double112022',
    'present_id': '2618',
}

def request_task(c,h,d):
    response = requests.post('https://hd.c.mi.com/tw/eventapi/api/raffle/drawprize', cookies=c, headers=h, data=d)
    print(response.text)

def fire_and_forget(c,h):
    threading.Thread(target=request_task, args=(c, h, data)).start()

while True:
    fire_and_forget(cookies_hytao,headers_hytao)
