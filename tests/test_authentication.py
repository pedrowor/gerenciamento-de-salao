"""Testes locais de cadastro, login e migração da tabela de usuários.

Execução:
    python -m unittest discover -s tests -v
"""

import os
import sqlite3
import tempfile
import unittest
from unittest.mock import Mock

from controller.app_controller import AppController
from model import database
from model.auth import authenticate_user, register_user


class AuthenticationTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_database = database.DATABASE_NAME
        database.DATABASE_NAME = os.path.join(
            self.temp_dir.name, "database.db"
        )
        database.setup_database()

    def tearDown(self):
        database.DATABASE_NAME = self.original_database
        self.temp_dir.cleanup()

    def test_no_default_account_is_created(self):
        with sqlite3.connect(database.DATABASE_NAME) as conn:
            count = conn.execute("SELECT COUNT(*) FROM usuarios").fetchone()[0]
        self.assertEqual(count, 0)

    def test_registration_and_password_authentication(self):
        self.assertTrue(register_user("pedro_test", "a-strong-password"))
        self.assertTrue(authenticate_user("pedro_test", "a-strong-password"))
        self.assertFalse(authenticate_user("pedro_test", "wrong-password"))
        self.assertFalse(authenticate_user("unknown", "a-strong-password"))

        with sqlite3.connect(database.DATABASE_NAME) as conn:
            stored = conn.execute(
                "SELECT password_hash FROM usuarios WHERE username = ?",
                ("pedro_test",),
            ).fetchone()[0]
        self.assertNotIn("a-strong-password", stored)
        self.assertTrue(stored.startswith("pbkdf2_sha256$"))

    def test_duplicate_username_and_invalid_password(self):
        self.assertTrue(register_user("my_user", "secure-pass-1"))
        self.assertFalse(register_user("my_user", "secure-pass-2"))
        with self.assertRaises(ValueError):
            register_user("another_user", "short")

    def test_migration_preserves_existing_data_and_blocks_legacy_login(self):
        # Simula a estrutura da versão original.
        with sqlite3.connect(database.DATABASE_NAME) as conn:
            conn.execute("DROP TABLE usuarios")
            conn.execute(
                "CREATE TABLE usuarios "
                "(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL)"
            )
            conn.execute("INSERT INTO usuarios(username) VALUES ('neide')")
            conn.execute(
                "INSERT INTO agendamentos "
                "(nome, data, servico) VALUES (?, ?, ?)",
                ("Cliente Teste", "2026-11-01 14:00:00", "Cabelo"),
            )

        database.setup_database()
        with sqlite3.connect(database.DATABASE_NAME) as conn:
            legacy = conn.execute(
                "SELECT password_hash FROM usuarios WHERE username = 'neide'"
            ).fetchone()
            appointments = conn.execute(
                "SELECT COUNT(*) FROM agendamentos"
            ).fetchone()[0]

        self.assertIsNone(legacy[0])
        self.assertEqual(appointments, 1)
        self.assertFalse(authenticate_user("neide", "any-password"))
        self.assertTrue(register_user("nova_conta", "new-pass-123"))
        self.assertTrue(authenticate_user("nova_conta", "new-pass-123"))

    def test_controller_rejects_mismatched_confirmation(self):
        controller = AppController.__new__(AppController)
        result = controller.handle_register_event(
            "pedro", "valid-pass-123", "different-pass"
        )
        self.assertEqual(result[0], False)


if __name__ == "__main__":
    unittest.main()
