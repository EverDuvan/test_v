import pandas as pd
from sqlalchemy.engine import create_engine
from dotenv import load_dotenv
import os
import requests
import time
import threading
load_dotenv()
df_lock = threading.Lock()

def proxy_check(proxy, df, df_urls):
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

def get_df(db: str, table, column=[]):
    """
    [get dataframe from postgres]
    return: pandas-df
    """
    a = eval(os.getenv("DB"))
    db=a[db]
    engine = create_engine('postgresql+psycopg2://{}:{}@{}:{}/{}'.format
                           (db['DB_USER'], 
                            db['DB_PASS'], 
                            db['DB_IP'], 
                            db['DB_PORT'], 
                            db['DB_NAME']))
    query= f'SELECT * from {table}'
    df = pd.read_sql_query(query, engine)
    if column != []:
        df=df[column]
    return df

def send_df_append(dataframe ,db , table):
    a = eval(os.getenv("DB"))
    db=a[db]
    engine = create_engine('postgresql+psycopg2://{}:{}@{}:{}/{}'.format
                            (db['DB_USER'], 
                                db['DB_PASS'], 
                                db['DB_IP'], 
                                db['DB_PORT'], 
                                db['DB_NAME']))
    dataframe.to_sql(table, 
                        engine, 
                        schema='public', 
                        if_exists='append', 
                        index=False, 
                        chunksize = 10)
    print ('¡Done!')

def send_df_replace(dataframe, db, table):
    a = eval(os.getenv("DB"))
    db=a[db]
    engine = create_engine('postgresql+psycopg2://{}:{}@{}:{}/{}'.format
                            (db['DB_USER'], 
                                db['DB_PASS'], 
                                db['DB_IP'], 
                                db['DB_PORT'], 
                                db['DB_NAME']))
    dataframe.to_sql(table,
                        engine,
                        schema='public',
                        if_exists='replace',
                        index=False,
                        chunksize = 10)
    print ('¡Done!')

