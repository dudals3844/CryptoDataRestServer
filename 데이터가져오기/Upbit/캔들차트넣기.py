import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from tqdm import tqdm
from pathlib import Path
from multiprocessing.pool import Pool


def start(file):
    sess = requests.Session()
    adapter = requests.adapters.HTTPAdapter(pool_connections=100, pool_maxsize=100)
    sess.mount('http://', adapter)

    print(file)
    data = pd.read_pickle(file)
    datas_dict = data.to_dict('records')
    insert_url = 'http://127.0.0.1:8000/upbit/candle/'
    response = sess.post(insert_url, json=datas_dict)
    print(response.text)
    # for data in datas_dict:
    #     response = sess.post(insert_url, data=data)
    #     print(response.text)


if __name__ == "__main__":
    files = list(Path('data').glob('*.pkl'))
    pool = Pool(10)
    pool.map(start, files)
    pool.close()
    pool.join()
