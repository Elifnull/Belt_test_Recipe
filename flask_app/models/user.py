from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.recipe import Recipe
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
Letter_pattern = re.compile("^[a-zA-Z]+$")

class User:
    db = "recipes"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data['password']
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.recipes = []

    @classmethod
    def get_all_recipies_users(cls):
        query="SELECT * FROM users LEFT JOIN recipes ON user.id = recipes.user_id"
        result = connectToMySQL(cls.db).query_db(query)
        return result
    @classmethod
    def get_with_email(cls,data):
        query="SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL(cls.db).query_db(query,data)
        user = (cls(result[0]))
        return user

    @classmethod
    def get_with_id(cls,data):
        query="SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL(cls.db).query_db(query,data)
        user = (cls(result[0]))
        return user

    @classmethod
    def get_users_recipes(cls,data):
        query="SELECT * FROM users LEFT JOIN recipes ON users.id = recipes.user_id WHERE users.id = %(id)s"
        result= connectToMySQL(cls.db).query_db(query,data)
