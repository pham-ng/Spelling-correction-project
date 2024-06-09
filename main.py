from SpellingCorrection.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from SpellingCorrection.logging import logger
from SpellingCorrection.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME= "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>> stage  {STAGE_NAME} >>>>>>>> started <<<<<<<<<<") 
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>>>>> stage  {STAGE_NAME} >>>>>>>> completed <<<<<<<<<< \n\nx========x")
except Exception as e:
    logger.error(f"An error occurred in {STAGE_NAME} stage: {e}")
    raise e


STAGE_NAME= "Data Validation Stage"
try:
    logger.info(f">>>>>>>>> stage  {STAGE_NAME} >>>>>>>> started <<<<<<<<<<") 
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info(f">>>>>>>>> stage  {STAGE_NAME} >>>>>>>> completed <<<<<<<<<< \n\nx========x")
except Exception as e:
    logger.error(f"An error occurred in {STAGE_NAME} stage: {e}")
    raise e