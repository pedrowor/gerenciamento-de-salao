# Changelog

This file records small, verified project maintenance changes. Unreleased changes are reviewed in pull requests before merging.

## Unreleased

### Fixed
- Appointment lists and reports now show a dash when a stored service price is missing instead of raising a formatting error.
- Loading an appointment for editing now leaves the price input blank when its database value is missing.

### Tests
- Added focused, headless regression tests for missing prices and normal numeric prices.
