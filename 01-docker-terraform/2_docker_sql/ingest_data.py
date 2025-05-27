#!/usr/bin/env python
# coding: utf-8

# import libraries
import os
import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db 
    url = params.url
    table_name = params.table_name

    # output the csv 
    csv_name = 'output.csv'


    os.system(f'wget {url} -O {csv_name}')

    #connecting to the database
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # read csv
    df_iter = pd.read_csv(csv_name, compression='gzip', iterator=True, chunksize=100000)

    # next chunk of data
    df = next(df_iter)

    # parse dates to datetimes and convert to dataframes
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)

    # create table and insert only the columns
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    # insert data to the database
    df.to_sql(name=table_name, con=engine, if_exists='append')

    while True:
        try:
            t_start = time()

            df = next(df_iter)

            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)

            df.to_sql(name=table_name, con=engine, if_exists='append')

            t_end = time()
            print('inserted another chunk... took %.3f seconds' % (t_end - t_start))

        except StopIteration:
            print("All chunks inserted.")
            break

if __name__ == '__main__':  
    
    parser = argparse.ArgumentParser(
                        description='Ingest CSV data to postgres'
                        )

    parser.add_argument('--user', help='username for postgres')
    parser.add_argument('--password',  help=' password for postgres')
    parser.add_argument('--host',  help='host for postgres')
    parser.add_argument('--port', help=' port for postgres')
    parser.add_argument('--db',  help='database name for postgres')
    parser.add_argument('--table_name', help=' name of the table where we will write the results to')
    parser.add_argument('--url',  help='url of the csv file')


    args = parser.parse_args()

    main(args)



