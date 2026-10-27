# Lab 5 — Reflection

## 1. What did you learn from static code analysis?

I learned that static analysis tools can identify code-quality, style, maintainability, and security issues without requiring the program to be executed. Pylint checks code quality, Flake8 checks style, and Bandit detects potential security vulnerabilities.

## 2. Which issue was the most serious, and why?

The shell command injection risk was the most serious issue because constructing shell commands from external input can allow unintended commands to execute. Unsafe pickle deserialization was also important because loading untrusted pickle data can execute malicious code.

## 3. How did you fix the identified issues?

I replaced unsafe pickle loading with JSON persistence, removed shell-based email execution, changed mutable default arguments to safe initialization, added docstrings, adopted snake_case naming, specified UTF-8 encoding, and corrected formatting and return statements.

## 4. What did you learn about testing and maintaining code?

I learned that code should be checked both before and after changes. I ran the original program and saved the initial analysis reports, then corrected the issues and reran the program and all three analysis tools. Comparing the reports helps verify whether code quality improved while preserving the main task-management functionality.
