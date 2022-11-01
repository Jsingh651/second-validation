from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Order:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.type = data['type']
        self.amount = data['amount']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all (cls):
        query = 'SELECT * FROM cookies'
        results = connectToMySQL('cookies_schema').query_db(query)
        orders = []
        for order in results:
            orders.append(cls(order))
        return orders

    @classmethod
    def create (cls,data):
        query = 'INSERT INTO cookies(name,type,amount) VALUES (%(name)s,%(type)s,%(amount)s);'
        return connectToMySQL('cookies_schema').query_db(query,data)

    @classmethod
    def update (cls,data):
        query = 'UPDATE cookies SET name = %(name)s, type = %(type)s, amount = %(amount)s WHERE id = %(id)s;'
        results = connectToMySQL('cookies_schema').query_db(query,data) 
        print('Results:', results)
        return results


    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM cookies WHERE id = %(id)s;'
        results =  connectToMySQL('cookies_schema').query_db(query,data)
        return cls(results[0])

    @staticmethod
    def validate(cookies):
        is_valid = True
        if len(cookies['name'])<= 2:
            flash('Name must be 3 characters')
            is_valid = False
        if int(cookies['amount']) <= 0:
            flash ('Must order 1 or more boxes')
            is_valid = False
        return is_valid
