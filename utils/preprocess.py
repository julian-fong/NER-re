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
    # print(sentence)
    try:
        tenant_re = "TENANT: "+re.search(r'agreement to lease(.*)tenant', sentence).group(1)[:100]
    except AttributeError:
        tenant_re = None
    try:
        tenant_re2 = "TENANT/LANDLORD: "+re.search(r'tenant(.*)landlord', sentence).group(1)[:100] #might have both tenant and landlord
    except AttributeError:
        tenant_re2 = None
    try:
        landlord_re = "LANDLORD: "+re.search(r'landlord:(.*)address of landlord', sentence).group(1)[:100]
    except AttributeError:
        landlord_re = None
    try:
        term_of_lease_re = "TERM OF LEASE: "+re.search(r"premises known as:(.*)3.", sentence).group(1)[:100]
    except AttributeError:
        term_of_lease_re = None
    try:
        address_re = "ADDRESS: "+re.search(r'premises known as:(.*)rent', sentence).group(1)[:100]
    except AttributeError:
        address_re = None

    return [tenant_re, tenant_re2, landlord_re, term_of_lease_re, address_re]

def normalize(sentence):
    sentence = sentence.replace("_", " ")
    return sentence.replace("\"", '\'').strip().lower()

def pretokenization(sentence):
    return sentence.split()

def tokenizer_(sentence):
    #figure out how to do this lol
    pass
    