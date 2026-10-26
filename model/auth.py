"""Cadastro e autenticação locais para o protótipo.

Senhas são armazenadas como PBKDF2-HMAC-SHA256 com salt aleatório.
Não existe mais usuário de demonstração com acesso sem senha.
"""

import hashlib
import hmac
import os
import re
from sqlite3 import Error, IntegrityError

from .database import connect_db


_ITERATIONS = 600_000
_USERNAME = re.compile(r"[A-Za-z0-9_-]{3,32}\Z")


def _password_hash(password):
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, _ITERATIONS
    )
    return f"pbkdf2_sha256${_ITERATIONS}${salt.hex()}${digest.hex()}"


def _password_matches(password, stored_hash):
    if not stored_hash:
        return False  # Contas antigas sem senha não podem entrar sem cadastro.
    try:
        method, iterations, salt_hex, digest_hex = stored_hash.split("$")
        if method != "pbkdf2_sha256":
            return False
        count = int(iterations)
        if count <= 0 or count > _ITERATIONS:
            return False
        actual = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), bytes.fromhex(salt_hex), count
        )
        return hmac.compare_digest(actual, bytes.fromhex(digest_hex))
    except (ValueError, AttributeError, TypeError):
        return False


def register_user(username, password):
    """Cria usuário e retorna False se o nome já estiver em uso.

    ValueError é usado para informar entradas inválidas à interface.
    """
    username = username.strip()
    if not _USERNAME.fullmatch(username):
        raise ValueError(
            "O usuário deve ter entre 3 e 32 caracteres: letras, números, _ ou -."
        )
    if not 8 <= len(password) <= 128:
        raise ValueError("A senha deve ter entre 8 e 128 caracteres.")

    connection = connect_db()
    if connection is None:
        raise RuntimeError("Não foi possível abrir o banco de dados.")
    try:
        connection.execute(
            "INSERT INTO usuarios (username, password_hash) VALUES (?, ?)",
            (username, _password_hash(password)),
        )
        connection.commit()
        return True
    except IntegrityError:
        return False
    finally:
        connection.close()


def authenticate_user(username, password):
    """Confere credenciais sem expor se o nome de usuário existe."""
    if not username or not password:
        return False
    connection = connect_db()
    if connection is None:
        return False
    try:
        cursor = connection.execute(
            "SELECT password_hash FROM usuarios WHERE username = ?",
            (username.strip(),),
        )
        row = cursor.fetchone()
        return bool(row and _password_matches(password, row[0]))
    except Error:
        return False
    finally:
        connection.close()
