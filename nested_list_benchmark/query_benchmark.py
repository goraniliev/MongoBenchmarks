# -*- coding: utf-8 -*-
from time import time
from pymongo import MongoClient
from nested_list_benchmark.config import fruits

__author__ = 'goran'

client = MongoClient()
db = client.benchmarks


def get_fruit_data_flat(fruit_name):
    data = db.fruits_flat.find({'fruit': fruit_name})
    return data


def get_fruit_data_nested(fruit_name):
    data = db.fruits_nested.find({'fruit': fruit_name})
    return data


def calculate_duration(get_func, times_entry_name: str):
    docs_count = 0
    before_time = time()
    for fruit in fruits:
        fruit_data = get_func(fruit)
        docs_count += len(list(fruit_data))
    after_time = time()
    flat_time = after_time - before_time
    db.times.insert_one({times_entry_name: flat_time, 'docs_retrieved': docs_count})


calculate_duration(get_fruit_data_flat, 'fruits_flat_get_time')
calculate_duration(get_fruit_data_nested, 'fruits_nested_get_time')
