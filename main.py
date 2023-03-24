import requests

API_KEY: str = '3a8b70e9-8122-4ab3-9590-49aa09a3a5ad'
START: int = 1
LIMIT: int = 300 # 1...5000
LISTING_STATUS: str = 'active' # active or inactive or untracked
SORT: str = 'cmc_rank' # 'id' or 'cmc_rank'

headers = {
    'Accepts' : 'application/json',
    'X-CMC_PRO_API_KEY' : API_KEY
}

try:
    response = requests.get(f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map?start={str(START)}&limit={str(LIMIT)}&sort={SORT}', headers=headers)
    jsoned = response.json()
    with open('data.txt', 'w') as f:
        for i in jsoned['data']:
            _ = f"{i['symbol']} : {i['name']}\n"
            f.write(_)

except requests.exceptions.ConnectionError as err:
    print(err)