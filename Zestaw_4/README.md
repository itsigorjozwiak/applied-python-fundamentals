# Applied Python Fundamentals
## Task set 4

> The fourth set focuses on ETL (Extract, Transform, Load) data pipelines, advanced Object-Oriented Programming (OOP) design patterns, and dynamic function overloading techniques.

* **Task 1:** Aviation data ETL pipeline: querying the OpenSky REST API, scheduling recurring network requests (`schedule`), managing persistent storage with `sqlite3`, data cleaning via `pandas`, and scatter plot visualization using `matplotlib`.
* **Task 2:** Advanced OOP architecture implementing the Abstract Factory design pattern for vehicle production, enforcing strict state encapsulation via abstract base classes (`abc.ABC`), `@property` decorators, and robust getter/setter/deleter validation.
* **Task 3:** Function overloading and single-dispatch polymorphism implementation using Python's standard library (`functools.singledispatch` and `functools.singledispatchmethod`).
* **Task 4:** Multiple dispatch pattern implementation for dynamic method resolution based on argument types and signatures, utilizing external libraries like `multipledispatch` and `plum`.

## Setup

**Dependencies:** Python 3.x, `requests`, `pandas`, `matplotlib`, `schedule`, `multipledispatch`, `plum-dispatch`, `pytest`. *(Note: `sqlite3` and `functools` are included in the standard Python library).*

```bash
# Install required packages
pip install -r requirements.txt

# Example of running the aviation data pipeline (Task 1)
python ZADANIE1/main.py
```
## Tests   
Unit tests are provided for tasks containing core architectural logic, validation rules, and database operations.

```bash
# Example of running tests for Task 1
pytest ZADANIE1/tests/
```
