from transformers import Seq2SeqTrainer
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch
from datasets import Dataset
import pandas as pd

from transformers import pipeline, set_seed, AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk, load_metric
import matplotlib.pyplot as plt
import pandas as pd
import torch
from tqdm import tqdm
import os

from transformers import Seq2SeqTrainer, Seq2SeqTrainingArguments


from transformers import DataCollatorForSeq2Seq
from transformers import Seq2SeqTrainingArguments
from transformers import Seq2SeqTrainer
from SpellingCorrection.entity import ModelTrainerConfig
class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def train(self):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

        dataset_spelling_correction= load_from_disk(self.config.data_path)

        training_args = Seq2SeqTrainingArguments(
            output_dir = self.config.root_dir,
            eval_strategy = self.config.eval_strategy,
            per_device_train_batch_size = self.config.per_device_train_batch_size,
            per_device_eval_batch_size = self.config.per_device_eval_batch_size,
            predict_with_generate = self.config.predict_with_generate,
            num_train_epochs = self.config.num_train_epochs,
            save_steps = self.config.save_steps,
            save_total_limit = self.config.save_total_limit,
            logging_steps = self.config.logging_steps,
            fp16 = self.config.fp16
        )
        
        trainer = Seq2SeqTrainer(
            model = model,
            tokenizer = tokenizer,
            args = training_args,
            data_collator= seq2seq_data_collator,
            train_dataset = dataset_spelling_correction["train"],
            eval_dataset = dataset_spelling_correction["validation"]
        )
        trainer.train()

        #save model:
        model.save_pretrained(os.path.join(self.config.root_dir,"bartpho-spelling-correction"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"bartpho-spelling-correction-tokenizer"))


