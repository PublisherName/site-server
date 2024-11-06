# Style Guide

This style guide provides guidelines for writing and formatting code, commit messages, and branch names to ensure consistency and maintainability across the project.


## Table of Contents
- [General Guidelines](#general-guidelines)
- [Commit Message Conventions](#commit-message-conventions)
- [Branch Naming Conventions](#branch-naming-conventions)
- [Code Formatting](#code-formatting)


## General Guidelines

- Write clear, concise, and self-explanatory code.
- Use meaningful variable and function names.
- Adhere to the language-specific best practices.
- Ensure your code is modular and reusable.
- Avoid code duplication and hard coded values
- Include docstrings for all functions, classes, and modules.

## Commit Message Conventions

Commit messages should be clear and descriptive. Follow these conventions for commit messages:

- Use the present tense ("Add feature" not "Added feature").
- Use the imperative mood ("Fix bug" not "Fixed bug").
- Keep the subject line (first line) under 50 characters.
- Separate subject from body with a blank line.
- Provide a detailed description of the changes in the body.
- Include references to relevant issues or pull requests.

### Examples:

```
feat: Add user authentication module

Implemented user login and registration functionalities.
Updated the database schema to include user credentials.
```

```
fix: Resolve crash on app startup

Fixed an issue causing the app to crash on startup due to a null pointer exception.
Closes #42.
```

## Branch Naming Conventions

Branch names should be descriptive and follow a consistent pattern. Use the following conventions for naming branches:

- Use lowercase letters and hyphens (`-`) to separate words.
- Include a prefix to indicate the type of branch:
  - `feat/` for new features
  - `fix/` for bug fixes
  - `chore/` for maintenance tasks
  - `docs/` for documentation updates
- Optionally, include an issue or ticket number for tracking (e.g., feat/issue-55-add-auth).

### Examples:

```
feat/add-user-authentication
fix/crash-on-startup
chore/update-dependencies
docs/improve-readme
```

## Code Formatting

Consistent code formatting enhances readability and maintainability. Follow these guidelines:

- Use [black](https://black.readthedocs.io/en/stable/) for automatic code formatting.
  - Default configuration with `max_line_length=79` and double quotes.
  - Target compatibility with Python 3.11.

- Use [flake8](https://flake8.pycqa.org/) for linting to ensure code quality.
  - Run `flake8` to catch unused variables and other potential issues.
  - Check for adherence to [PEP 8](https://peps.python.org/pep-0008/) and coding best practices.

- Use [isort](https://github.com/PyCQA/isort) to sort imports.
  - Align `isort` settings with `black` for consistent formatting.
  - Format multi-line imports using the "Vertical Hanging Indent" style.
  - Add 2 blank lines after import statements.
  - Combine `as` imports, grouping them together.

- Use [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks) for helpful pre-commit checks.
  - Flags any large files added to the repository.
  - Detects unresolved merge conflict markers in files.
  - Detects `print()` and `pdb` statements in Python code to prevent accidental commits of debug code.
  - Identifies and removes trailing whitespace for cleaner, more consistent formatting.

- Use [yamllint](https://github.com/adrienverge/yamllint) to format YAML files.
  - Limits lines to a maximum of 140 characters.
  - Allows at most one space inside braces and brackets.
  - Disallows spaces after colons and commas.
  - Disables linting and indentation checks for comments.
  - Disables requiring the document start marker (`---`) at the beginning of YAML files.
  - Allows a maximum of two consecutive empty lines.
  - Enables checks for duplicate keys in mappings (dictionaries) to prevent unintentional overwrites.
  - Disables checks enforcing explicit `true`/`false` values instead of `yes`/`no`.

- Use [pyupgrade](https://github.com/asottile/pyupgrade) to upgrade Python syntax automatically.
  - Enables updates for syntax supported from Python 3.7 onward.

- Use [codespell](https://github.com/codespell-project/codespell) to identify and fix common spelling errors.

## Before pushing your code, run the following command:

```bash
pre-commit run --all-files
```

By following this style guide, you contribute to a consistent and maintainable codebase, making it easier for everyone to collaborate and improve the project. Thank you for your contributions!
