import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging

@dataclass #decorator (use only if you want to define variables in class without init)
#(if you have functions in class use normall init style no decorator)
class DataIngestionConfig:
    train_data_path= os.path.join('artifacts','train.csv')
    test_data_path= os.path.join('artifacts','test.csv')
    raw_data_path= os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self) :
        self.ingestion_config= DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info("Entered the data_ingestion method or component")
        try:
            df=pd.read_csv('notebooks/data/stud.csv')
            logging.info('Reading data as dataframe completed')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train Test Split Initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Data Ingestion Completed")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            logging.info(e)
            raise CustomException(e,sys)
        
if __name__=='__main__':
    obj=DataIngestion()
    obj.initiate_data_ingestion()
