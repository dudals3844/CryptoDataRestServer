import time
import requests
import pandas as pd
import json
from tqdm import tqdm
from datetime import datetime
from multiprocessing.pool import ThreadPool
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# %%
session = requests.Session()
retry = Retry(connect=1000, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)


# %%
def start(ticker):
    url = "https://api.upbit.com/v1/trades/ticks"
    now = datetime.now().strftime("%Y-%m-%d")
    date_ranges = pd.date_range('2021-01-01', now, freq='3H')
    data_df = pd.DataFrame()
    for date in tqdm(date_ranges):
        params = {
            "market": ticker,
            "count": "200",
            "to": date,
        }
        response = session.get(url, params=params)
        response_dict = json.loads(response.text)
        data_df = pd.concat([data_df, pd.DataFrame(response_dict)])
        time.sleep(0.1)
    datas = data_df.to_dict('records')

    def insert(data):
        insert_url = 'http://127.0.0.1:8000/upbit/trades/'
        session.post(insert_url, data=data)

    pool = ThreadPool(processes=10)
    pool.map(insert, tqdm(datas))
    pool.close()
    pool.join()


# %%
ticker_url = 'http://127.0.0.1:8000/upbit/ticker/'
response = session.get('http://127.0.0.1:8000/upbit/ticker/')
ticker_df = pd.DataFrame(json.loads(response.text))
for ticker in ticker_df['market']:
    print(ticker)
    start(ticker)
