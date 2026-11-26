# Python LernArchiv (Modules 2 – 7)

![Python CI](https://github.com)

A structured collection of Python exercises, design patterns, and a modular, multi-threaded network monitoring CLI tool built during my software engineering studies in Magdeburg.

---

## Featured Project: `NetzwerkMonitor`

Located in [`NetzwerkMonitor/`](./NetzwerkMonitor), this modular CLI tool checks live TCP/443 availability and latency across multiple hosts concurrently.

- **Concurrent Scanning:** Uses `concurrent.futures.ThreadPoolExecutor` to probe all hosts in parallel.
- **Clean Architecture:** Separates data models (`models.py`), concurrent network probing (`scanner.py`), JSON/log persistence (`reporter.py`), and CLI orchestration (`main.py`).
- **Automated Testing & CI:** Verified with `pytest` unit/mock tests and executed automatically on every push via **GitHub Actions**.

### Quick Start

```bash
cd NetzwerkMonitor
python main.py
python -m pytest -v
```

---

## Curriculum Modules Overview

### Module 2 — Pythonic Data Processing & Iteration
- **`modul2_comprehensions.py`** — List, set, and dictionary comprehensions with filtering.
- **`modul2_generatoren.py`** — Memory-efficient data pipelines using `yield` and generator expressions.
- **`modul2_idiome.py`** — Pythonic idioms (`enumerate`, `zip`, `any`/`all`, unpacking).
- **`modul2_iteratoren.py`** — Custom iterator classes implementing `__iter__` and `__next__`.

### Module 3 — File Handling & Structured Data
- **`modul3_dateien.py`** — Safe file reading/writing with `pathlib` and UTF-8 encoding.
- **`modul3_json.py`** — Serialization, deserialization, and configuration parsing with `json`.

### Module 4 — Object-Oriented Programming (OOP)
- **`modul4_oop.py`** — Classes, encapsulation, `@property`, and dunder methods (`__str__`, `__repr__`).
- **`modul4_vererbung.py`** — Inheritance hierarchies, `super()`, and polymorphism (`Server` -> `DatabaseServer`).

### Module 5 — Modern Python Features
- **`modul5_context_manager.py`** — Custom resource management with `__enter__` / `__exit__` and `contextlib`.
- **`modul5_dataclasses.py`** — Clean immutable/mutable data containers with `@dataclass`.

### Module 6 — APIs, Concurrency & Parallelism
- **`modul6_api_client.py`** — Consuming REST APIs with error handling and timeouts.
- **`modul6_threading_lock.py`** — Preventing race conditions with `threading.Lock` and `ThreadPoolExecutor`.
- **`modul6_asyncio_vergleich.py`** — Direct performance benchmark comparing `threading` vs. `asyncio.gather`.
 
### Module 7 — Encodings, Structured Formats & CLI Automation

- **modul7_encoding_robust.py** — Explicit UTF-8 handling, text vs. binary modes (`str` vs. `bytes`), and resilient file reading with `errors="replace"`.
- **modul7_csv_json_yaml.py** — Reading, writing, and comparing flat tabular data (`csv`) against typed/hierarchical formats (`json`, `yaml.safe_load`).
- **modul7_json_datetime.py** — Serializing `datetime` objects to ISO-8601 strings in JSON (`default=str`, custom serializer, `datetime.fromisoformat()`).
- **modul7_argparse_logging.py** — Building reusable CLI scripts with `argparse` (`choices`, positional/optional flags) and `logging` separated from `stdout`.
- **modul7_idempotenz.py** — Designing idempotent automation scripts that verify state before writing so repeated scheduler runs never cause duplicate side effects.
- **modul7_backup_automation.py** — Unattended cross-platform backup script combining `subprocess.run` (`tar -czf`), `pathlib`, daily idempotency checks, `logging` with full tracebacks, and distinct exit codes.
### Module 8 — Data Science & Numerical Computing

- **modul8_numpy.py** — NumPy array creation (`np.array`, `np.arange`), vectorization, and benchmark comparing pure Python loops against `np.sum()`.
