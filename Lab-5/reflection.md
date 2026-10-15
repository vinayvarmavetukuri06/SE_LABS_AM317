# Lab 5: Static Code Analysis — Reflection

### 1. What is static code analysis, and how did it help in this project?

Static code analysis examines source code without executing it to identify potential bugs, security vulnerabilities, and coding-style problems. In this project, Pylint, Bandit, and Flake8 helped identify issues in the applicant tracking system before and after modification.

### 2. What is the difference between Pylint, Bandit, and Flake8?

Pylint checks overall code quality, naming conventions, documentation, and potential programming issues. Bandit identifies common security risks, such as unsafe use of `eval()` and insecure SQL query construction. Flake8 checks Python style rules, including line length, whitespace, and formatting.

### 3. What important issues were found and how were they fixed?

The original program used `eval()` to evaluate the salary limit and constructed an SQL insert query using an f-string. These were replaced with a numeric salary limit and parameterized SQL queries. Broad exception handling that silently ignored errors was removed. The code was also improved with descriptive docstrings, consistent function names, and safer file handling.

### 4. How did static analysis improve the program, and what are its limitations?

Static analysis improved the security, readability, and maintainability of the applicant tracking system. The final results showed a Pylint score of 10.00/10, no Bandit findings, and an empty Flake8 report. However, static analysis cannot guarantee that a program is completely correct, so the program must also be executed and tested to verify its behavior.