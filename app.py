import sys
from src.mlproject.logger import logging
from src.mlproject.components.data_ingestion import DataIngestion, DataIngestionConfig
from src.mlproject.exception import CustomException

if __name__=='__main__':
    logging.info('Testing Custom Exception')
        
    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info(CustomException(e,sys))
        raise CustomException(e,sys)