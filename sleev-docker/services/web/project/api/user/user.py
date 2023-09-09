from flask import jsonify, json
from project.models import db, User
from .user_aux import *
from datetime import datetime

def get_user_from_id(user_id: int):
    return User.query.filter_by(id=user_id).first()


def get_last_user_by_email(email_str: str):
    return User.query.filter_by(_email=email_str).order_by(User.created_at.desc()).first()


def delete_all_users():
    try:
        db.session.query(User).delete()
        db.session.commit()
        return jsonify({
            "msg": "deleted successfully",
            "error": "",
            "success": True,
            "data": ""
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "msg": "",
            "error": e.__str__(),
            "success": False,
            "data": ""
        }), 409


def add_user(first_name: str, last_name: str, email: str, password_str: str, scout_id:int, birth_date:datetime, scout_group:int, section:int, role:str) -> json:
    old_user: User = get_last_user_by_email(email_str=email)  
    if (old_user is not None):
        if (old_user.deleted_at is None):
            return jsonify({
                "msg": "",
                "error": "email already in use",
                "success": False,
                "data": old_user.to_dict()
            }), 409

    if not validate_email(email):
            return jsonify({
                "msg": "",
                "error": "email is invalid",
                "success": False,
                "data": ""
            }), 409
        
    email_split:list = email.split("@")
    if not validate_password(password_str):
            return jsonify({
                "msg": "",
                "error": "password is invalid",
                "success": False,
                "data": ""
            }), 409
    password_hash:str = hash_password(password_str)
    if section is None:
        section = calculate_section(birth_date)
    if role is None:
        role = 'scout'
    
    new_user = User(first_name=first_name, last_name=last_name, email=email, domain=email_split[1], password_hash=password_hash, scout_id=scout_id, scout_group=scout_group, birth_date=birth_date, section=section, role=role)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "msg": "User created successfully",
        "success": True,
        "data": new_user.to_dict()
    }), 200


def delete_user(email: str) -> json:
    user: User = get_last_user_by_email(email_str=email)

    if (user is None):
        return jsonify({
            "msg": "",
            "error": "user does not exist",
            "success": False,
            "data": ""
        }), 409

    if (user.deleted_at is not None):
        return jsonify({
            "msg": "",
            "error": "user is already deleted",
            "success": False,
            "data": user.to_dict()
        }), 409

    user.delete()

    return jsonify({
        "msg": "User deleted successfully",
        "success": True,
        "data": user.to_dict()
    }), 200


def migrate_users():
    try:
        users = db.session.query(User)
        for u in users:
            u.is_admin = False
            u.is_super_admin = False
            u.auth_token = User.generate_token()
        db.session.commit()
        
        return jsonify({
            "msg": "Users migrated successfully",
            "success": True,
            "data": ''
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "msg": "",
            "error": e.__str__(),
            "success": False,
            "data": ""
        }), 409


def login_user(email: str, password: str) -> json:
    if not validate_email(email):
        return jsonify({
            "msg": "",
            "error": "email is invalid",
            "success": False,
            "data": ""
        }), 409

    user: User = get_last_user_by_email(email_str=email)  
    if (user is None or user.deleted_at is not None):
        return jsonify({
            "msg": "",
            "error": "user not found",
            "success": False,
            "data": ""
        }), 409

    if not (validate_password(password) and check_password(user=user, password=password)):
        return jsonify({
            "msg": "",
            "error": "invalid password",
            "success": False,
            "data": ""
        }), 409
        
    
    return jsonify({
        "msg": "User fetched successfully",
        "success": True,
        "data": user.to_dict()
    }), 200

