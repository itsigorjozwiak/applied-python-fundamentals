# Applied Python Fundamentals
## Task set 5

> The fifth set focuses on the implementation and visualization of core sorting algorithms, algorithmic problem-solving, and building automated data collection pipelines interacting with real-world public APIs.

* **Task 1:** Algorithmic performance analysis and dynamic visualization (`matplotlib`) of sorting algorithms (Merge Sort, Quick Sort, Tim Sort) using `numpy` for data generation and benchmarking.
* **Task 2:** Advanced algorithmic problem-solving targeting specific competitive programming challenges (from HackerRank) focusing on the `reduce` function and mathematical optimizations (maximizing values under constraints).
* **Task 3:** Traficar fleet monitor: fetching live data from the REST API via scheduled GitHub Actions, storing it in `sqlite3`, and analyzing daily vehicle movement and fuel consumption.

## Setup

**Dependencies:** Python 3.x, `numpy`, `matplotlib`, `requests`, `pytest`. *(Note: `sqlite3` and `functools` are included in the standard Python library).*

```bash
# Install required packages
pip install -r requirements.txt

# Example of running Task 3
cd ZADANIE3
python analyze_fleet.py
```

## Tests   
Unit tests are provided for tasks containing core algorithmic logic, edge-case validation, and data parsing.

```bash
# Example of running tests for Task 1
pytest ZADANIE1/tests/
```
