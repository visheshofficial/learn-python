# Introduction

## What is Unit Testing?

Spot Bugs Early: Unit testing helps identify bugs early in the development process.
Prevent Bugs in Production: Testing ensures that bugs are caught before the code is deployed.
Safety Nets: Multiple layers of testing provide safety nets to maintain code quality.

### Levels of Testing

Unit Testing: Tests individual functions or methods.
Component Testing: Tests at the library or compiled binary level.
System Testing: Tests the external interfaces of a system, which is a collection of subsystems.
Performance Testing: Evaluates the performance of the system.

### Unit Testing

Function-Level Testing: Tests individual functions.
Comprehensive Test Cases: Write tests for all positive and negative scenarios of a function.
Test Suites: Group related tests together for better organization.
Development Environment: Execute tests in the development environment.
Automated Execution: Automate the execution of tests for efficiency.

### Example Unit Test

```python
def add(a, b):
    return a + b

def test_add():
    # Setup
    a = 1
    b = 2
    # Action
    result = add(a, b)
    # Assert
    assert result == 3
```

## What is TDD?

- Test-Driven Development (TDD) is a software development approach where tests are written before the actual code.
- no need to write all test cases at once. start one at a time and write the code to make it pass at production grade.
- tests abd production code both are written together
- gives you confidence to make changes in code
- gives immediate feedback
- documents what the code is doing
- drives good object-oriented design

- was created by Kent Beck in the late 1990s as part of the Extreme Programming (XP) methodology.

### Principles of TDD

Write Tests First: Write a test before writing the code that makes the test pass.
Refactor: Refactor the code to improve its structure and remove duplication.
Repeat: Continuously repeat the cycle of writing tests, writing code, and refactoring.

### TDD Workflow

RED - write a failing test
GREEN - write the minimum code to make the test pass
REFACTOR - refactor the code to improve its structure, make it clean and remove duplication

### 3 Laws of TDD

- You are not allowed to write any production code unless it is to make a failing unit test pass.
- You are not allowed to write any more of a unit test than is sufficient to fail, and compilation failures are failures.
- You are not allowed to write any more production code than is sufficient to pass the one failing unit test.
