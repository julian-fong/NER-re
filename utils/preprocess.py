import pandas as pd
import re
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

def decompose_sentence(sentence):
    tenant_re = "TENANT: "+re.search(r'Agreement to Lease(.*)TENANT', sentence).group(1)
    tenant_re2 = "TENANT: "+re.search(r'TENANT(.*)LANDLORD', sentence).group(1) #might have both tenant and landlord
    landlord_re = "LANDLORD: "+re.search(r'LANDLORD:(.*)ADDRESS OF LANDLORD', sentence).group(1)
    term_of_lease_re = "TERM OF LEASE: "+re.search(r"premises known as:(.*)3.", sentence).group(1)
    address_re = "ADDRESS: "+re.search(r'premises known as:(.*)RENT', sentence).group(1)

    return [tenant_re, tenant_re2, landlord_re, term_of_lease_re, address_re]

def normalize(sentence):
    return sentence.replace("\"", '\'').strip().lower()

def pretokenization(sentence):
    return sentence.split()

def tokenizer_(sentence):
    #figure out how to do this lol
    pass
    