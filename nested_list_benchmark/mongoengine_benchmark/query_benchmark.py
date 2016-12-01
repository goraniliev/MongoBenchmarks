# -*- coding: utf-8 -*-
from time import time
from pymongo import MongoClient
from nested_list_benchmark.config import mongoengine_connect, fruits
from nested_list_benchmark.mongoengine_benchmark.model import FruitModelFlat, FruitModelNested

__author__ = 'goran'

mongoengine_connect()
client = MongoClient()
db = client.benchmarks

def get_fruit_data_flat(fruit):
    return FruitModelFlat.get_data_for_fruit(fruit)

def get_fruit_data_nested(fruit):
    return FruitModelNested.get_data_for_fruit(fruit)

def calculate_duration(get_func, times_entry_name: str):
    docs_count = 0
    before_time = time()
    for fruit in fruits:
        fruit_data = get_func(fruit)
        docs_count += len(list(fruit_data))
    after_time = time()
    flat_time = after_time - before_time
    db.times.insert_one({times_entry_name: flat_time, 'docs_retrieved': docs_count})

calculate_duration(get_fruit_data_flat, 'fruit_mongoengine_flat_get_time')
calculate_duration(get_fruit_data_nested, 'fruit_mongoengine_nested_get_time')
