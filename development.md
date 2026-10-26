# Development Notes

This project is a desktop appointment management application built with Python, Tkinter, and SQLite.

## Local Setup

1. Install Python with Tkinter support.
2. Clone the repository.
3. Run `python main.py` from the project root.

## Testing

Run the automated tests using:

```bash
python -m unittest discover -s tests -v
```

## Development Workflow

Changes should be developed on short-lived branches.

Before merging into `main`, review the code changes and run the relevant tests.

Significant changes should be documented in both `CHANGELOG.md` and `CHANGELOG.pt-BR.md`.
