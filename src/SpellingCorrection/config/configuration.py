from SpellingCorrection.constants import*
from SpellingCorrection.utils.common import read_yaml,create_directories

from SpellingCorrection.entity import (DataIngestionConfig, DataValidationConfig,
                                       DataTransformationConfig,ModelTrainerConfig)




import os
import yaml
from dataclasses import dataclass 
from pathlib import Path
CONFIG_FILE_PATH = Path("config/config.yaml")  # Replace with the actual file path
PARAMS_FILE_PATH = Path("params.yaml")

class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH):
        
            self.config = read_yaml(config_filepath)
            self.params = read_yaml(params_filepath)

            create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config= DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        return data_ingestion_config
    
    def get_data_validation_config(self)->DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE = config.STATUS_FILE,
            ALL_REQUIRED_FILE = config.ALL_REQUIRED_FILE
        )
        return data_validation_config
    
    def get_data_transformation_config(self)->DataTransformationConfig:
            config =self.config.data_transformation
            create_directories([config.root_dir])

            data_transformation_config= DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            tokenizer_name = config.tokenizer_name
            )
            return data_transformation_config
    
    
    def get_model_trainer_config(self)-> ModelTrainerConfig:
        config= self.config.model_trainer
        params = self.params.Seq2SeqTrainingArguments
        create_directories([config.root_dir])

        model_trainer_config= ModelTrainerConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            model_ckpt = config.model_ckpt,

            evaluation_strategy = params.evaluation_strategy,
            eval_steps = params.eval_steps,
            per_device_train_batch_size = params.per_device_train_batch_size,
            per_device_eval_batch_size = params.per_device_eval_batch_size,
            num_train_epochs = params.num_train_epochs,
            save_steps = params.save_steps,
            save_total_limit = params.save_total_limit,
            logging_steps = params.logging_steps,
            predict_with_generate = params.predict_with_generate,
            fp16 = params.fp16
            
        )
        return model_trainer_config
    
    


