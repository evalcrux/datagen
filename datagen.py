# Python script to generate random data and documents to send to elasticsearch

from random_words import RandomWords
from datetime import datetime
from elasticsearch import Elasticsearch
import requests
import os
from random import *
rw = RandomWords()

# ES Connection Info
conn_str = 'CONNECTION_STRING'
es = Elasticsearch([conn_str])
print("Connected", es.info())

# Data Model Configuration
num_fields = 10
max_words = 10
num_docs = 1000

# Create Fields
doc = {}
docs = []
for count in range(num_fields):
    word_list = []
    for rand_word_count in range(randrange(1,max_words)):
        word_list.append(rw.random_word())
    field = 'field'+str(count)
    sentence = ' '.join(word for word in word_list)
    print(field,'-',sentence)
    doc[field] = sentence
print(doc)
docs.append(doc)
res = es.index(index="test-index", doc_type='doc', id=1, body=doc)
print(res['created'])
