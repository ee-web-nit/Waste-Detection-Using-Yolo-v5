import os
from dataclasses import dataclass
from datetime import datetime
from WasteDetection.constants.training_pipeline import *

@dataclass
class TrainingPipelineConfig:
    artifact_dir: str = ARTIFACTS_DIR


training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()



@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME)

    feature_store_dir: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR)

    data_download_url: str = DATA_DOWNLOAD_URL 

@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_VALIDATION_DIR_NAME)

    validation_status_file_dir: str = os.path.join(data_validation_dir, DATA_VALIDATION_STATUS_FILE)

    required_files_list = DATA_VALIDATION_ALL_REQUIRED_FILES