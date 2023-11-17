import concurrent.futures
import pandas as pd
import os
from datetime import datetime
import time
from func import *

def main():
    # Start counting.
    start_time = time.time()

    df_urls = get_df('proxies_test', 'urls')
    df_proxies= get_df('proxies_test', 'proxies')
    proxies = df_proxies['ip'].tolist()

    # create DF columns = ['proxies', 'working'] + df_urls.columns
    df = pd.DataFrame(columns=['proxies', 'working'] + df_urls.columns.tolist())

    # Number of threads
    num_threads = 4
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Utilizar función partial para pasar parámetros adicionales
        partial_proxy_check = lambda proxy: proxy_check(proxy, df, df_urls)
        executor.map(partial_proxy_check, proxies)

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

if __name__ == "__main__":
    main()
