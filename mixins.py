import requests
import json


def get_all_news():
    repsonse = requests.get('http://13.51.255.44/news/?limit=1000')
    if repsonse.status_code == 200:
        return json.loads(repsonse.text)['results']
    else:
        return 'Error'
    
def get_retrieve_news(slug):
    response = requests.get('http://13.51.255.44/news/' + slug)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return 'Error'


def get_all_univers():
    response = requests.get('http://13.51.255.44/university/?limit=1000')
    if response.status_code == 200:
        return json.loads(response.text)['results']
    else:
        return 'Error'
    

def get_about_univers(id):
    response = requests.get(f'http://13.51.255.44/university/{id}/')
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return 'Error'
    
def get_news_univer(id):
    response = requests.get(f'http://13.51.255.44/university/{id}/news/?limit=1000')
    if response.status_code == 200:
        print(response.text)
        return json.loads(response.text)['results']
    else:
        return 'Error'