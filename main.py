"""
Integrating with API.
"""
import os
import json
import jinja2
import requests
GITHUB_URL = 'https://api.github.com/user'
github_token = os.environ.get('GITHUB_TOKEN')
github_id = os.environ.get('GITHUB_ID')
r = requests.get(GITHUB_URL, auth=(github_id, github_token),
                 timeout=2.5)
data_1 = json.loads(r.text)
with open('github.json', 'w', encoding='utf-8') as file:
    file.write(str(data_1).replace("'", '"').replace('True', '"True"').
               replace('False', '"False"').
               replace('None', '"None"'))
vk_token = os.environ.get('VK_TOKEN')
vk_id = os.environ.get('VK_ID')
VK_URL = 'https://api.vk.com/method/users.get'
r = requests.get(VK_URL, params={'access_token': vk_token, 'user_ids': vk_id,
                                 'v': 5.131}, timeout=2.5)
data_2 = json.loads(r.text)
with open('vk.json', 'w', encoding='utf-8') as file:
    file.write(str(data_2).replace("'", '"').replace('True', '"True"').
               replace('False', '"False"'))
with open('index.html', encoding='utf-8') as file:
    template = jinja2.Template(file.read())
with open('github.json', encoding='utf-8') as file:
    github_data = json.load(file)
with open('vk.json', encoding='utf-8') as file:
    vk_data = json.load(file)
page = template.render(name=vk_data['response'][0]['first_name'],
                       surname=vk_data['response'][0]['last_name'],
                       github=github_data['html_url'])
with open('index.html', 'w+', encoding='utf-8') as file:
    file.write(page)
