from project.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

def check_password(user:User, password:str) -> bool:
    return check_password_hash(user.password_hash, password)

def hash_password(password:str) -> str:
    return generate_password_hash(password)

def validate_password(password:str) -> bool:
    # TODO.txt:add an evaluator
    return len(password) > 4

def validate_email(email:str) -> bool:
    # TODO.txt: add an evaluator
    return "@" in email

def calculate_section(birth_date:datetime):
    current_date = datetime.now()
    age:int = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))

    if age in range(6, 10):
        return 1
    elif age in range(10, 14):
        return 2
    elif age in range(14, 18):
        return 3
    elif age in range(18, 23):
        return 4

    return 0