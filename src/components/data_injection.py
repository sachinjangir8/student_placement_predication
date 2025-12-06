import os
import sys  # to get the details of the exception ,custom exception
from src.exception import CustomException
#                 1. Loading raw data into the pipeline
#                 2. Validating the input data
#                 3. Storing the raw data
#                 4. Splitting data     into-  ( Train set , Test set )
from src.logger import logging  
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
# in data injestion where we have to store the train data, test data and raw data that we will make the dataclass for that

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationconfig

@dataclass   #use the dataclass decorator to only define the variables
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','data.csv')

# now we will create a class for data ingestion
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()  # we will create an object of DataIngestionConfig class

    def initiate_data_ingestion(self):
        # it is used to initiate the data ingestion like loading the data from the source (database-utils ) and splitting it into train and test set
        logging.info("Entered the data ingestion method or component")
        try:
            # here we can read the data from anywhere like database or s3 bucket but for now we will read it from a csv file
            df=pd.read_csv('notebook/data/stud.csv')
            logging.info("Read the dataset as dataframe ")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            # to make the directory if it is not present
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train test split initiated")
            # now we will split the data into train and test set
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            # now we will save the train and test set into the respective paths 
            # train data to csv me change krke train_set me save krna hai
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            logging.info("Exception occured at data ingestion stage")
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    # the data path we are getting from data ingestion will be passed to data transformation
    data_transformation.initiate_data_transformation(train_data,test_data)