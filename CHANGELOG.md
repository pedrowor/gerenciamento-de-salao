# Changelog

This file records small, verified project maintenance changes. Unreleased changes are reviewed in pull requests before merging.

## Unreleased

### Added
- Added a Create Account dialog and password sign-in for local users.
- Store passwords with a unique salt and PBKDF2-HMAC-SHA256.
- Upgrade existing user tables without deleting appointments.

### Changed
- Removed the default username-only login. Accounts from older databases without a password hash cannot sign in until a new account is created.

### Tests
- Added registration, authentication, duplicate username, and database migration tests.

### Fixed
- Appointment lists and reports now show a dash when a stored service price is missing instead of raising a formatting error.
- Loading an appointment for editing now leaves the price input blank when its database value is missing.

### Tests
- Added focused, headless regression tests for missing prices and normal numeric prices.
