import sys, os
from WasteDetection.logger import logging
from WasteDetection.exception import AppException
from WasteDetection.components.data_ingestion import DataIngestion
from WasteDetection.entity.config_entity import (DataIngestionConfig)
from WasteDetection.entity.artifact_entity import (DataIngestionArtifact)
from WasteDetection.components.data_validation import DataValidation
from WasteDetection.entity.config_entity import DataValidationConfig
from WasteDetection.entity.artifact_entity import DataValidationArtifact

class TrainingPipeline:
    def __init__(self):
         self.data_ingestion_config = DataIngestionConfig()
         self.data_validation_config = DataValidationConfig()


    def start_data_ingestion(self) -> DataIngestionArtifact:
         try:
              logging.info("Entered the start_data_ingestion method of TrainingPipeline class")
              logging.info("Getting the data from url")
              data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)

              data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
              logging.info("Got the data from url")
              logging.info("Exited the start_data_ingestion method of TrainingPipeline class")
              return data_ingestion_artifact
         except Exception as e:
              raise AppException(e, sys) 
     
    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
         try:
              logging.info("Entered the start_data_validation method of TrainingPipeline class")
              data_validation = DataValidation(data_validation_config=self.data_validation_config, data_ingestion_artifact=data_ingestion_artifact)

              data_validation_artifact = data_validation.initiate_data_validation()
              logging.info("Performed data validation operation on the ingested data")
              logging.info("Exited the start_data_validation method of TrainingPipeline class")
              return data_validation_artifact
         except Exception as e:
              raise AppException(e, sys)
         
    def run_pipeline(self) -> None:
         try:
              data_ingestion_artifact = self.start_data_ingestion()
              data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
         except Exception as e:
              raise AppException(e, sys)