'''
Created on 2018. 1. 16.

@author: SDS
'''

if __name__ == '__main__':
    pass

from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch(['192.168.0.11:9200'])
a = es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})
print(a)

b = es.get(index="my-index", doc_type="test-type", id=42)['_source']
print(b)
