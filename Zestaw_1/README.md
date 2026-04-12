# Applied Python Fundamentals
## Task set 1

> The first set focuses on algorithmic problem-solving, API consumption and local LLM integration.

* **Task 1:** Prime factorization algorithm optimized for large integers via CLI.
* **Task 2:** Real-time Run-Length Encoding (RLE) compression with a sliding-window terminal animation (`collections.deque`, generators).
* **Task 3:** Interactive digital terminal clock built with character matrices and dynamic screen refreshing.
* **Task 4:** Real-time weather data aggregator consuming the `wttr.in` REST API (JSON parsing).
* **Task 5:** Local Large Language Model (LLM) chat interface integrating with Ollama (Llama 3.2:1b) via HTTP requests.

## Setup

**Dependencies:** Python 3.x, `requests`, `pytest`.

```bash
# Install required packages
pip install -r requirements.txt

# Example of running Task 4
python ZADANIE4/zadanie4.py
```
## Tests   
Unit tests are provided for tasks containing core algorithmic logic.

```bash
# Example of running tests for Task 1
pytest ZADANIE1/tests/
```
