import os

import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv('BASE_URL')

def search_yandex_eda(text: str):
    response = requests.post(
        f'{BASE_URL}/api/v1/menu/search',
        json={"region_id": 1,
              "place_slug": "perekrestok",
              "text": text,
              "location": {"lat": 55.7106035,
                           "lon": 37.743341}
              }
    )
    if response.ok:
        return response.json()
    else:
        response.raise_for_status()
