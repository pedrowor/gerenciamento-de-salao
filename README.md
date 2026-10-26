# Salon Appointment Manager

An educational desktop appointment-management application built with **Python, Tkinter, and SQLite**, organized into controller, model, and view modules. This repository is a **fork of [jorgemdt/gerenciamento-de-salao](https://github.com/jorgemdt/gerenciamento-de-salao)**. Consult the commit history to distinguish upstream work from changes in this fork.

## Features visible in the source
- Username-only demo login
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

The application creates a local `database.db` file when needed. The database setup creates a demonstration username **`neide`**.

## Project structure
```text
main.py                 Application entry point
controller/             UI events, workflow, and validation
model/                  SQLite access and appointment operations
view/                   Login, main window, and report window
```

## Important limitations
- **This is an educational prototype, not a production-ready salon system.** The login checks only whether a username exists; it does not authenticate with a password.
- The database file is created relative to the working directory.
- No automated test suite or deployment procedure is documented here.
- Actual installation and end-to-end GUI behavior should be tested in your target environment.

## Skills demonstrated
Python modules, Tkinter GUI events, SQL/SQLite persistence, parameterized queries, CRUD operations, input validation, and separation of responsibilities.

## Future improvements
Add secure password authentication, automated tests, collision checks for appointments, improved error reporting, and packaging instructions.

## Credits
Forked from [jorgemdt/gerenciamento-de-salao](https://github.com/jorgemdt/gerenciamento-de-salao). Check the repository's license and commit history for attribution and contribution details.
