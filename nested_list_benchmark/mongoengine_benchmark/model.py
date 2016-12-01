# -*- coding: utf-8 -*-
from mongoengine import Document, StringField, IntField, FloatField, ListField, EmbeddedDocument

__author__ = 'goran'


class FruitModelFlat(Document):
    meta = {
        'collection': 'fruit_model_flat',
        'allow_inheritance': False,
        'abstract': False,
        'indexes': [
            'fruit'
        ]
    }

    fruit = StringField()
    timestamp = IntField()
    price = FloatField()
    total_items = IntField()
    total_price = FloatField()

    @classmethod
    def get_data_for_fruit(cls, fruit_name):
        return cls.objects(fruit=fruit_name)

    def to_dict(self):
        return {
            'fruit': self.fruit,
            'timestamp': self.timestamp,
            'price': self.price,
            'total_items': self.total_items,
            'total_price': self.total_price
        }

class DayDataModel(EmbeddedDocument):
    timestamp = IntField()
    price = FloatField()
    total_items = IntField()
    total_price = FloatField()


class FruitModelNested(Document):
    meta = {
        'collection': 'fruit_model_nested',
        'allow_inheritance': False,
        'abstract': False,
        'indexes': [
            'fruit'
        ]
    }

    fruit = StringField(unique=True)
    days_data = ListField()

    @classmethod
    def add_day_data_for_fruit(cls, fruit, days_data):
        obj = FruitModelNested.objects(fruit=fruit).first()
        if obj:
            obj.update(push__days_data=days_data)
        else:
            new_obj = FruitModelNested(fruit=fruit, days_data=[days_data])
            new_obj.save()

    @classmethod
    def get_data_for_fruit(cls, fruit_name):
        return cls.objects(fruit=fruit_name)
