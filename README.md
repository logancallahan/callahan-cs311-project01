# Project 1: The Speed Cache
Logan Callahan — CS 311

## Overview
This project implements a thread-safe Least Recently Used (LRU) cache in Python. When the cache is full, inserting a new entry removes the entry that has gone the longest without being used.

A dictionary maps keys directly to doubly linked-list nodes. The list keeps the most recently used entry at the front and the least recently used entry at the back. Both get and put use a single lock to protect concurrent access.

## Requirements
- Python 3
- No third-party packages are required.
- Use a positive integer for the cache capacity.

## Files
- lru_cache.py: Cache lookup, insertion, updates, eviction, and locking.
- doubly_linked_list.py: Nodes and linked-list operations.
- test_lru.py: Unit tests.
- simulate_hitrate.py: Cache hit-rate simulation.
- verify_project1.py: Project verification.
- DESIGN.md or accompanying design sketch: Map-to-node relationship.

## Running the Project
Open a terminal in the  folder.

Run the unit tests:
```bash
python3 -m unittest test_lru.py
```

Run the hit-rate simulation:
```bash
python3 simulate_hitrate.py
```

Run the project verifier:
```bash
python3 verify_project1.py
```

## Usage Example
```python
from lru_cache import LRUCache, _MISSING

cache = LRUCache(2)
cache.put("A", 10)
cache.put("B", 20)

print(cache.get("A"))  # 10; A becomes most recently used

cache.put("C", 30)     # Evicts B
print(cache.get("B") is _MISSING)  # True
```

## Behavior and Complexity
Reading or updating an existing entry moves it to the front. A missing key returns the _MISSING sentinel, allowing None to remain a valid stored value.

Dictionary access gives expected O(1) lookup. Moving a node and removing the least recently used node require a fixed number of pointer changes. Therefore, get and eviction take expected O(1) time, and put takes expected amortized O(1) time. Storage is O(capacity).