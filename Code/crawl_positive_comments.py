import requests
import pandas as pd
import time
import random
from tqdm import tqdm

cookies = {
    '_trackity': 'd3aa0598-e174-0439-4be0-7122a29d6acc',
    '_hjSessionUser_522327': 'eyJpZCI6Ijg1NGJlYTc0LTY5NjUtNTlkNi04MzAwLWI2ODA0YTNlNzdiMyIsImNyZWF0ZWQiOjE2NTY0MTMzNjI1NzUsImV4aXN0aW5nIjp0cnVlfQ==',
    '_ga': 'GA1.1.110661371.1709825024',
    'TOKENS': '{"access_token":"KQOCLxBbhTDnFisNEtRva0H32G9dJlcI"}',
    '_gcl_au': '1.1.1226893276.1711780792',
    '__RC': '5',
    'dtdz': '50a0b3d6-c997-5a47-9e68-9c7b3d125ee4',
    '__iid': '749',
    '__su': '0',
    '__R': '3',
    '__tb': '0',
    'TIKI_RECOMMENDATION': 'e4c1abb4c38863c4c4979ba19a80b9b3',
    'delivery_zone': 'Vk4wMzkwMDYwMDE=',
    'tiki_client_id': '110661371.1709825024',
    '_hjSession_522327': 'eyJpZCI6IjIyZmIyM2ViLTkwZmEtNGI4Mi1iNzU5LTM3YmFkODlmNWI3NCIsImMiOjE3MTIzMjM3OTQxMTgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=',
    '_fbp': 'fb.1.1712323825475.127913418',
    '__IP': '1907225281',
    'TKSESSID': '7f784ef6417325b4a75cb6ef11b9dc09',
    '__adm_upl': '{"time":1712327407,"_ups":"0-1605141705245451352"}',
    '__uif': '__uid%3A1686745802091496460%7C__ui%3A-1%7C__create%3A1711780794',
    'cto_bundle': 'oBDmwV94cElvRnFySEk3MSUyQjdHWHZpME56SGNnSGFvSyUyRmhLUUxGV2RnT3pUWlI2MW1SMEtzTmtVZUt4ZVZpeDZ5bEp5MktSWDduV25Md3lTdHRmeVNFcjVycXMwdFJGSTJSSjNYajBBbGVXWktMSmJlMml3d0NncWFzSmtFbWM2WUJMTHF1NkkxMzhuMTdqS3MzNHBUaDZRTmFBJTNEJTNE',
    'amp_99d374': 's1fBVRxLFHYxAiebYk6zrJ...1hqn771ff.1hqnb0d03.7s.9b.h7',
    '_ga_S9GLR1RQFJ': 'GS1.1.1712323790.4.1.1712327776.44.0.0'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Referer': 'https://tiki.vn/chuyen-xu-lang-biang-4-bau-vat-o-lau-dai-k-rahlan-p580326.html?spid=580334',
    'x-guest-token': 'KQOCLxBbhTDnFisNEtRva0H32G9dJlcI',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

params = {
    'product_id': '74021317',
    'sort': 'stars|4|5',
    'page': '1',
    'limit': '5',
    'include': 'comments,contribute_info,attribute_vote_summary'
}

def comment_parser(json):
    d = dict()
    d['product_id'] = json.get('product_id')
    d['cmt_id'] = json.get('id')
    d['title'] = json.get('title')
    d['content'] = json.get('content')
    d['thank_count'] = json.get('thank_count')
    d['customer_id']  = json.get('customer_id')
    d['rating'] = json.get('rating')
    d['created_at'] = json.get('created_at')
    d['customer_name'] = json.get('created_by').get('name')
    d['purchased_at'] = json.get('created_by').get('purchased_at')
    return d


df_id = pd.read_csv('product_id_ncds.csv')
p_ids = df_id.id.to_list()
result = []
for pid in tqdm(p_ids, total=len(p_ids)):
    params['product_id'] = pid
    print('Crawl comment for product {}'.format(pid))
    for i in range(5):
        params['page'] = i
        response = requests.get('https://tiki.vn/api/v2/reviews', headers=headers, params=params, cookies=cookies)
        if response.status_code == 200:
            print('Crawl comment page {} success!!!'.format(i))
            for comment in response.json().get('data'):
                result.append(comment_parser(comment))
df_comment = pd.DataFrame(result)
df_comment.to_csv('comments_data_ncds_positive.csv', index=False, encoding='utf-8-sig')
