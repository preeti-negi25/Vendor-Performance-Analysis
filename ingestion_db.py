import pandas as pd 
import os 
from sqlalchemy import create_engine
import logging
import time 
logging.basicConfig(
    filename='logs/ingestion.db.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode = "a"
)
engine = create_engine('sqlite:///inventory.db')

def ingest_db(df , table_name, engine): 
    'this fun will ingest dataframe to database table'
    df.to_sql(table_name, con = engine , if_exists = 'replace' , index = False , chunksize = 100000 )
    
def load_raw_data():
    'this fun will load cvs as dataframe and ingest into database '
    start = time.time()
    for file in os.listdir('data'):
        if '.csv' in file:
            df = pd.read_csv('data/' + file , low_memory= True)
            logging.info(f'Ingesting{file}in db')
            ingest_db(df , file[:-4], engine)
            
    end = time.time()
    total_time = round((end-start)/60,2)
    logging.info('Ingestion Complete')
        
    logging.info(f'\nTotal Time Taken : {total_time}minutes')
if __name__ ==  '__main__': 
    load_raw_data()