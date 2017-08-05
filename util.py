

from sqlalchemy import create_engine
import psycopg2 as pq
import pandas as pd
import numpy as np
golf_db = 'postgresql://localhost:5432/golf'


def scale_plot_size(factor=1.5):
    import matplotlib as mpl
    default_dpi = mpl.rcParamsDefault['figure.dpi']
    mpl.rcParams['figure.dpi'] = default_dpi*factor
    
def exec_sql(sqlTxt, result=False):  
    with pq.connect(golf_db) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sqlTxt) 
            if result:
                return [row for row in cursor] 
        
def pd_from_sql(sqlTxt, params = None):
    with pq.connect(golf_db) as conn:
        return pd.read_sql_query(sqlTxt, conn, params = params)
    
def np_to_sql(arr, table):
    df = pd.DataFrame(arr)
    with pq.connect(golf_db) as conn:
        df.to_sql(table, conn, if_exists='append')
        
def np_from_sql(sqlTxt, params=None):
    return pd_from_sql(sqlTxt, params).as_matrix()

scale_plot_size(1.5)