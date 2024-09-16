

import requests
from bs4 import BeautifulSoup

def extract_info(profile_url):
    response = requests.get(profile_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    info = {}

    # Location
    location = soup.find('li', class_='t-16 t-black t-normal break-words')
    if location:
        location = location.text.strip()
    else:
        location = 'Not Available'
    info['location'] = location

    # Phone Number
    phone_number = soup.find('a', class_='link-without-visited-state')
    if phone_number and phone_number['href'].startswith('tel:'):
        phone_number = phone_number['href'].replace('tel:', '')
    else:
        phone_number = 'Not Available'
    info['phone_number'] = phone_number

    # Username
    username = profile_url.split('/')[-1].split('-')[0]
    info['username'] = username

    return info

# Test the function with 10 LinkedIn profile URLs
profile_urls = [
    '(link1)',
    '(link2)',
    '(link3)',
    '(link4)',
    '(link5)',
    '(link6)',
    '(link7)',
    '(link8)',
    '(link9)',
    '(link10)'
]

for url in profile_urls:
    info = extract_info(url)
    print(info)
    print('------------------------')
