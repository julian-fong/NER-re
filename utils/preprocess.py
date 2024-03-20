import pandas as pd
from transformers import AutoTokenizer, AutoModel

model_name = "dslim/distilbert-NER"
tokenizer = AutoTokenizer.from_pretrained(model_name)

feature_classes = {
    0:'0',
    1:'B-Landlord',    
    2:'I-Landlord',
    3:'B-Tenant',
    4:'I-Tenant',
    5:'B-Address',
    6:'I-Address',
    7:'B-Rent',
    8:'I-Rent',
    9:'B-LeaseDate',
    10:'I-LeaseDate',
}

def normalize(sentence):
    return sentence.replace("\"", '\'').strip().lower()

def pretokenization(sentence):
    return sentence.split()

def tokenizer_(sentence):
    #figure out how to do this lol
    pass
    