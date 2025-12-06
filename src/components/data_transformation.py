import os
import sys  # to get the details of the exception ,custom exception
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransformationconfig:
    # this is the path where we will save the preprocessor object /model object
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    """ 
     This class is responsible for data transformation
    """

    def __init__(self):
        # create an object of DataTransformationconfig class this will help us to get the file path
        self.data_transformation_config=DataTransformationconfig()

    def get_data_transformer_object(self):
        try:
            logging.info("Data Transformation initiated")
            # we will define which columns should be scaled and which should be encoded
            numerical_columns=['writing_score','reading_score']
            categorical_columns=['gender',
                                 'race_ethnicity',
                                 'parental_level_of_education',
                                 'lunch',
                                    'test_preparation_course'
                                 ]
            # now we will create the pipeline for numerical and categorical columns
            num_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median')), # heandling missing values
                    ('scaler',StandardScaler())
                ]
            )
            cat_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('one_hot_encoder',OneHotEncoder()),
                    ('scaler',StandardScaler(with_mean=False))
                ]
            )
            logging.info("Numerical and categorical pipeline completed")

            # to combine the both pipelines
            preprocessor=ColumnTransformer(
                [
                    ('num_pipeline',num_pipeline,numerical_columns),
                    ('cat_pipeline',cat_pipeline,categorical_columns)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessor object")
            preprocessor_obj=self.get_data_transformer_object()

            target_column_name='math_score'
            numerical_columns=['writing_score','reading_score']
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]
            # now we will apply the preprocessor object on train and test dataframe
            logging.info("Applying preprocessor object on training and testing dataframe")
            
            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)

            # now we will concatenate the input feature array and target feature array
            train_arr=np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]
            logging.info("Saved preprocessor object")  

            # we will write a utility function to save the preprocessor object 
            from src.utils import save_object
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj
            )
            # save the preprocessor object
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )


        except Exception as e:
            raise CustomException(e,sys)