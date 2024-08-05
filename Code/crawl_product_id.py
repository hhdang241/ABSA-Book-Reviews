import requests
import time
import random
import pandas as pd

# cookies = {
#     '_trackity': 'd3aa0598-e174-0439-4be0-7122a29d6acc',
#     '_hjSessionUser_522327': 'eyJpZCI6Ijg1NGJlYTc0LTY5NjUtNTlkNi04MzAwLWI2ODA0YTNlNzdiMyIsImNyZWF0ZWQiOjE2NTY0MTMzNjI1NzUsImV4aXN0aW5nIjp0cnVlfQ==',
#     '_ga': 'GA1.1.110661371.1709825024',
#     'TOKENS': '{"access_token":"8jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY"}',
#     '_gcl_au': '1.1.1226893276.1711780792',
#     '__RC': '5',
#     'dtdz': '50a0b3d6-c997-5a47-9e68-9c7b3d125ee4',
#     '__iid': '749',
#     '__su': '0',
#     '__R': '3',
#     '__tb': '0',
#     'TIKI_RECOMMENDATION': 'e4c1abb4c38863c4c4979ba19a80b9b3',
#     'delivery_zone': 'Vk4wMzkwMDYwMDE=',
#     'tiki_client_id': '110661371.1709825024',
#     '_hjSession_522327': 'eyJpZCI6IjIyZmIyM2ViLTkwZmEtNGI4Mi1iNzU5LTM3YmFkODlmNWI3NCIsImMiOjE3MTIzMjM3OTQxMTgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=',
#     '_fbp': 'fb.1.1712323825475.127913418',
#     '__IP': '1907225281',
#     'TKSESSID': '7f784ef6417325b4a75cb6ef11b9dc09',
#     '__adm_upl': '{"time":1612347407,"_ups":"0-1605141705245451352"}',
#     '__uif': '__uid%3A1686745802091496460%7C__ui%3A-1%7C__create%3A1711780794',
#     'amp_99d374': 's1fBVRxLFHYxAiebYk6zrJ...1hqn771ff.1hqn906g9.71.8e.ff',
#     '_ga_S9GLR1RQFJ': 'GS1.1.1712323790.4.1.1712325664.43.0.0'
# }

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Referer': 'https://tiki.vn/nha-sach-tiki/c8322?seller=53660',
    'x-guest-token': 'KQOCLxBbhTDnFisNEtRva0H32G9dJlcI',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

params = {
    'limit': '40',
    'include': 'advertisement',
    'aggregations': '2',
    'version' : 'home-persionalized',
    'trackity_id': 'd3aa0598-e174-0439-4be0-7122a29d6acc',
    'category': '8322',
    'page': '1',
    'seller': '53660',
    'urlKey': 'nha-sach-tiki',
    # 'q' : 'nguyễn nhật ánh',
    
}

product_id = []
for i in range(1, 8):
    params['page'] = i
    response = requests.get('https://tiki.vn/api/v2/products', headers=headers, params=params)#, cookies=cookies)
    if response.status_code == 200:
        print('request success!!!')
        for record in response.json().get('data'):
            product_id.append({'id': record.get('id')})
    time.sleep(random.randrange(3, 10))

df = pd.DataFrame(product_id)
df.to_csv('product_id_ncds.csv', index=False)
