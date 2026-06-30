import hashlib
import os
import sqlite3

DB_NAME = "users.db"



def init_db():
    """Creates the database and table if they do not exist yet."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                salt TEXT NOT NULL
            )
        """
        )
        conn.commit()


def hash_password(password, salt=None):
    """Securely hashes a password using a unique salt and SHA-256."""
    if salt is None:
        salt = os.urandom(16).hex()  # Creates a unique random salt
    # Combine salt and password, then hash them
    hashed = hashlib.sha256((salt + password).encode("utf-8")).hexdigest()
    return hashed, salt


def register_user(username, password):
    """Registers a new user. Returns True if successful, False if username exists."""
    username = username.strip()
    if not username or not password:
        return False, "Username and password cannot be empty."

    hashed_pwd, salt = hash_password(password)

    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)",
                (username, hashed_pwd, salt),
            )
            conn.commit()
            return True, "Registration successful!"
    except sqlite3.IntegrityError:
        return False, "Username already exists."


def login_user(username, password):
    """Checks credentials. Returns True if correct, False if invalid."""
    username = username.strip()

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT password_hash, salt FROM users WHERE username = ?",
            (username,),
        )
        result = cursor.fetchone()

        if result:
            stored_hash, salt = result
            # Hash the typed password with the user's stored salt
            check_hash, _ = hash_password(password, salt)

            if check_hash == stored_hash:
                return True, "Login successful!"

        return False, "Invalid username or password."


init_db()
