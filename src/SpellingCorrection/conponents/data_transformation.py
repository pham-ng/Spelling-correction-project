import os
import torch

from SpellingCorrection.logging import logger
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import Seq2SeqTrainingArguments
from transformers import Seq2SeqTrainer
from tqdm.notebook import tqdm
from datasets import load_from_disk

from SpellingCorrection.entity import DataTransformationConfig
from pathlib import Path

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
    
    def convert_examples_to_features(self, example_batch):
        # Làm sạch dữ liệu để loại bỏ các giá trị không hợp lệ
        example_batch['noisy_phrases'] = [str(x) if x is not None else "" for x in example_batch['noisy_phrases']]
        example_batch['sentence']= [str(x) if x is not None else "" for x in example_batch['sentence']]
        input_encodings=self.tokenizer(example_batch['noisy_phrases'], max_length=128,padding="max_length", truncation=True)

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['sentence'],max_length=128, padding="max_length", truncation=True)

        return {
            "input_ids": input_encodings['input_ids'],
            "attention_mask": input_encodings['attention_mask'],
            "labels": target_encodings['input_ids'],
        }
    def convert(self):
        
        dataset=load_from_disk(self.config.data_path)
        dataset_pt=dataset.map(self.convert_examples_to_features, batched=True)
        dataset_pt.save_to_disk(os.path.join(self.config.root_dir, "dataset"))
