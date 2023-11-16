import pandas as pd
from sqlalchemy.engine import create_engine
from dotenv import load_dotenv
import os
load_dotenv()

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

