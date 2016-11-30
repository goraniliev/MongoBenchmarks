# -*- coding: utf-8 -*-
from time import sleep
import traceback
import mongoengine

__author__ = 'goran'

MONGODB_CONNECTION = "mongodb://localhost:27017"
MONGODB_NAME = "benchmarks"

def mongoengine_connect(host=MONGODB_CONNECTION, db_name=MONGODB_NAME):
    while True:
        try:
            mongoengine.connect(host=host, db=db_name)
            break
        except Exception:
            print(traceback.format_exc())
            sleep(2)

fruits = ['apple', 'pear', 'orange', 'banana', 'lemon', 'strawberry', 'blackberry', 'peach', 'pineapple', 'mango']
