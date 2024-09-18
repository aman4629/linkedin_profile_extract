import requests
from bs4 import BeautifulSoup

def extract_info(profile_url):
    try:
        response = requests.get(profile_url)
        response.raise_for_status()  # Check for HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {profile_url}: {e}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    info = {}

    # Location
    location = soup.find('li', class_='t-16 t-black t-normal break-words')
    info['location'] = location.text.strip() if location else 'Not Available'

    # Phone Number
    phone_number = soup.find('a', class_='link-without-visited-state')
    if phone_number and phone_number['href'].startswith('tel:'):
        info['phone_number'] = phone_number['href'].replace('tel:', '')
    else:
        info['phone_number'] = 'Not Available'

    # Username
    info['username'] = profile_url.split('/')[-1].split('-')[0]

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
    if info:
        print(info)
        print('------------------------')


