# Applied Python Fundamentals
## Task set 2

> The second set explores advanced data structures, robust exception handling, concurrent programming (GIL vs. free-threaded), and scientific computing.

* **Task 1:** Deeply nested data structure traversal and modification algorithm for mixed types (lists, tuples, dicts).
* **Task 2:** Roman/Arabic numeral converter implementing strict exception handling and input validation (`ValueError`, `try-except`).
* **Task 3:** Wikipedia REST API scraper featuring regex-based text parsing, fixed-width formatting, and word frequency analysis (`collections.Counter`).
* **Task 4:** Multithreaded numerical Pi calculator benchmarking Python 3.14's experimental free-threaded (no-GIL) execution mode.
* **Task 5:** Mathematical function visualizer and symbolic mathematics evaluator using `numpy`, `matplotlib`, and `SymPy` (`lambdify`).

## Setup

**Dependencies:** Python 3.14 (recommended for Task 4), `requests`, `numpy`, `matplotlib`, `sympy`, `pytest`.

```bash
# Install required packages
pip install -r requirements.txt

# Example of running Task 3 (Wikipedia scraper)
python ZADANIE3/zadanie3.py
```

## Tests   
Unit tests are provided for tasks containing core algorithmic logic and exception validation.

```bash
# Example of running tests for Task 2
pytest ZADANIE2/tests/
```
