import json
import random

def get_user_data(username):
    # Intentional SQL Injection vulnerability for Security Agent
    query = f"SELECT * FROM users WHERE username = {username}"
    print("Executing:", query)

def check_value(val):
    # Intentional Pylint anti-pattern (!= None)
    if val != None:
        return True
    return False
