from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
import re
from flask import flash

class Recipe:
    db="recipes"
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.date_made = data["date_made"]
        self.under_30 = data["under_30"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
    
    @classmethod
    def save_recipe(cls,data):
        query="INSERT INTO recipes (name, description, instructions, date_made, under_30, created_at, updated_at) VALUES ( %(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, Now(), Now());"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def update_recipe(cls,data):
        query="UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made =%(date_made)s, under_30 = %(under_30)s, updated_at = Now() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_all_recipe(cls):
        query="SELECT * FROM recipes"
        result = connectToMySQL(cls.db).query_db(query)
        print(result)
        all_recipes = []
        for d in result:
            all_recipes.append(cls(d))
            print(d)
        return all_recipes
    
    @classmethod
    def delete(cls,data):
        query="DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)