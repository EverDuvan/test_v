import concurrent.futures
import pandas as pd
import requests
import os
from datetime import datetime
import time
import threading
from db_con import *

# Start counting.
start_time = time.time()

df_urls = get_df('proxies_test', 'urls')
df_proxies= get_df('proxies_test', 'proxies')
proxies = df_proxies['ip'].tolist()

# create DF columns = ['proxies', 'working'] + df_urls.columns
df = pd.DataFrame(columns=['proxies', 'working'] + df_urls.columns.tolist())

df_lock = threading.Lock()

def proxy_check(proxy):
    # Add 'http://' if not exist
    if not proxy.startswith('http://'):
        proxy = 'http://' + proxy
    for _, row in df_urls.iterrows():
        url = row['url_category']
        try:
            response = requests.get(url, proxies={'http': proxy, 'https': proxy}, timeout=5)
            if response.status_code == 200:
                print(f'Proxy {proxy} working with URL {url}')
                with df_lock:
                # add working status to DF
                    df.loc[len(df)] = [proxy.replace("http://", ""), True] + row.tolist()
            else:
                print(f'Proxy {proxy} not working with URL {url}')
                # add working status to DF
                with df_lock:
                    df.loc[len(df)] = [proxy.replace("http://", ""), False] + row.tolist()
        except Exception as e:
            print(f'Proxy {proxy} not working with URL {url}')
            # add working status to DF
            with df_lock:
                df.loc[len(df)] = [proxy.replace("http://", ""), False] + row.tolist()
    return df

# Number of threads
num_threads = 4

with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    executor.map(proxy_check, proxies)

# Actual date time 
now = datetime.now()
now_str = now.strftime("%Y-%m-%d_%H-%M-%S")
# Making the folder 'proxies_test' if it doesn't exist
if not os.path.exists('proxies_test'):
    os.makedirs('proxies_test')

# save DataFrame to DB
send_df_replace(df, 'proxies_test', 'result')

# save DataFrame to Excel
df.to_excel(f'proxies_test/{now_str}.xlsx', index=False)

# Calculate the elapsed time.
elapsed_time = (time.time() - start_time)/60
print(f'Elapsed time in total: {round(elapsed_time, 2)} Minutes.')
print(f"DF correctly saved in 'proxies_test/{now_str}.xlsx'")
