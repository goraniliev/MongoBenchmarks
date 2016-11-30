# -*- coding: utf-8 -*-
from random import randint
from time import time
from pymongo import MongoClient
from nested_list_benchmark.config import fruits

__author__ = 'goran'

DOCS_TOTAL = 100000

docs = []
nested_docs = {}

for day in range(DOCS_TOTAL):
    timestamp = randint(10000000000, 90000000000)
    price = randint(1, 1000)
    fruit = fruits[randint(0, len(fruits) - 1)]
    total_items = randint(1, 1000)
    total_price = total_items * price

    doc = {
        'timestamp': timestamp,
        'fruit': fruit,
        'price': price,
        'total_items': total_items,
        'total_price': total_price
    }

    docs.append(doc)

    nested_docs.setdefault(fruit, [])
    nested_docs[fruit].append({
        'timestamp': timestamp,
        'price': price,
        'total_items': total_items,
        'total_price': total_price
    })

client = MongoClient()
db = client.benchmarks
before_insertion = time()
db.fruits_flat.create_index('fruit')
db.fruits_flat.insert_many(docs)
after = time()
insertion_time = after - before_insertion
db.times.insert_one({'fruits_flat_insertion_time': insertion_time, 'docs_inserted': DOCS_TOTAL})

nested_docs = [{'fruit': fruit, 'data': data} for fruit, data in nested_docs.items()]
before = time()
db.fruits_nested.create_index('fruit')
db.fruits_nested.insert_many(nested_docs)
after = time()
insertion_time = after - before
db.times.insert_one({'fruits_nested_insertion_time': insertion_time, 'docs_inserted': DOCS_TOTAL})
