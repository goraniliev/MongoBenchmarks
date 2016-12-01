# -*- coding: utf-8 -*-
from random import randint
from nested_list_benchmark.config import fruits, mongoengine_connect
from nested_list_benchmark.mongoengine_benchmark.model import FruitModelFlat, FruitModelNested, DayDataModel

__author__ = 'goran'

DOCS_TOTAL = 100000

mongoengine_connect()

for day in range(DOCS_TOTAL):
    timestamp = randint(10000000000, 90000000000)
    price = randint(1, 1000)
    fruit = fruits[randint(0, len(fruits) - 1)]
    total_items = randint(1, 1000)
    total_price = total_items * price

    doc = FruitModelFlat(fruit=fruit, timestamp=timestamp, price=price, total_items=total_items, total_price=total_price)
    doc.save()

    # nested_doc_day_data = DayDataModel(timestamp=timestamp, price=price, total_items=total_items, total_price=total_price)
    nested_doc_day_data = {
        'timestamp': timestamp,
        'price': price,
        'total_items': total_items,
        'total_price': total_price
    }
    FruitModelNested.add_day_data_for_fruit(fruit, nested_doc_day_data)
