import bcrypt
import os

def crear_password(password: str) -> tuple:
    salt = bcrypt.gensalt()
    password_hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return password_hashed, salt

def verificar_password(password: str, password_registrada: bytes, salt: bytes) -> bool:
    password_hashed = bcrypt.hashpw(password.encode('utf-8'), salt)  # Volver a hashear usando el mismo salt
    return password_hashed == password_registrada  # Comparar hashes