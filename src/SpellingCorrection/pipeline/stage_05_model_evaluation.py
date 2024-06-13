from SpellingCorrection.config.configuration import ConfigurationManager
from SpellingCorrection.logging import logger
from SpellingCorrection.conponents.model_evaluation import ModelEvaluation

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evaluation_config=ModelEvaluation(model_evaluation_config)
        model_evaluation_config.evaluate()

