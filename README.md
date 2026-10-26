# Salon Appointment Manager

An educational desktop appointment-management application built with **Python, Tkinter, and SQLite**, organized into controller, model, and view modules. This repository is a **fork of [jorgemdt/gerenciamento-de-salao](https://github.com/jorgemdt/gerenciamento-de-salao)**. Consult the commit history to distinguish upstream work from changes in this fork.

## Features visible in the source
- Local account registration and password sign-in
- Add, list, edit, and delete appointments
- Record customer name, phone, email, appointment date/time, service, and price
- Display an appointment report in a separate window
- SQLite database initialization on startup

## Requirements
- Python 3 with Tkinter support (Tkinter may need a separate OS package on some Linux distributions)
- No external Python packages are imported in the inspected source

## Run locally
From the repository root:

```bash
python main.py
```

The application creates a local `database.db` file when needed.

### First-time login
1. Start the app with `python main.py`.
2. Select **Criar conta** (Create account).
3. Choose a unique username (3–32 letters, numbers, `_` or `-`) and a password of at least 8 characters.
4. Confirm the password and select **Cadastrar**.
5. Sign in with your newly created account.

There is **no shared default username or password**. Passwords are stored as salted PBKDF2-HMAC-SHA256 hashes, not plaintext.

### Existing databases
The application keeps the existing `database.db` and appointment records and adds a password-hash column to older user tables. Legacy username-only accounts (such as `neide`) **cannot sign in without a password**; create a new account using a different username. Existing bookings stay in the same local database. Back up `database.db` before upgrading.

## Project structure
```text
main.py                 Application entry point
controller/             UI events, workflow, and validation
model/                  SQLite access and appointment operations
view/                   Login, main window, and report window
```

## Important limitations
- **This is a local educational prototype, not a production-ready multi-user system.** All registered accounts access the same appointment database; there is no per-user data isolation, recovery flow, or account administration.
- The database file is created relative to the working directory.
- Focused unit tests are available with `python -m unittest discover -s tests -v`. There is no deployment procedure.
- Actual installation and end-to-end GUI behavior should be tested in your target environment.

## Skills demonstrated
Python modules, Tkinter GUI events, SQL/SQLite persistence, parameterized queries, CRUD operations, input validation, and separation of responsibilities.

## Future improvements
Add per-user access controls, password recovery, appointment collision checks, improved error reporting, and packaging instructions.

## Credits
Forked from [jorgemdt/gerenciamento-de-salao](https://github.com/jorgemdt/gerenciamento-de-salao). Check the repository's license and commit history for attribution and contribution details.
