# Lab 5: Static Code Analysis — Issues

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe eval() usage | Security — Medium | 14 | Evaluates a salary rule as Python code, which can execute unsafe expressions. | Pass a numeric salary limit directly instead of evaluating a string. |
| SQL injection risk | Security — Medium | 8 | Applicant data is inserted into an SQL query using an f-string. | Use parameterized SQL queries with placeholders. |
| Broad exception handling | Error handling — Low | 28 | Catches every Exception and silently ignores errors with pass. | Catch expected SQLite errors and handle or report them appropriately. |
| Unused variable | Code quality | 15 | total_seen is assigned but never used. | Remove the unused variable or use it meaningfully. |
| Incorrect function naming | Style | 7, 24, 31, 38 | Function names use camelCase instead of snake_case. | Rename functions to add_applicant, update_status, export_report and count_by_status. |
| Long lines | Style | 4, 8, 13, 26, 39 | Several lines exceed the 79-character limit reported by Flake8. | Split long statements across multiple lines. |
| Missing docstrings | Code quality | Multiple | The module and functions lack explanatory docstrings. | Add concise module and function docstrings. |
| Unsafe file handling pattern | Code quality | 32–35 | The report file is opened without a with statement and closed manually. | Use with open(...) to ensure the file closes correctly. |
| Trailing whitespace | Style | 15 | A line contains unnecessary whitespace at the end. | Remove trailing whitespace. |