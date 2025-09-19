from pymongo.mongo_client import MongoClient
import os
import sys
from dotenv import load_dotenv
load_dotenv()
import certifi
MONGO_DB_URL = os.getenv("MONGODB_URL_KEY")
import json

uri = MONGO_DB_URL
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from network_security.exceptions.exception import NetworkSecurityException
from network_security.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except:
            raise NetworkSecurityException(e,sys)
        
    def cv_to_json_converter(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(uri, tlsCAFile=ca)
            self.database = self.mongo_client[self.database]

            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)

if __name__ =='__main__':
    FILE_PATH = "/home/vaibhav-mishra/ML/project2/Network_Data/dataset.csv"
    DATABASE = "SpikeSiegel"
    Collection = "Network_Data"
    networkobj = NetworkDataExtract()
    records = networkobj.cv_to_json_converter(FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(f"Total number of records inserted in mongodb is : {no_of_records}")
# print(uri)
# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=ca)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)