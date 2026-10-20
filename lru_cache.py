"""
Project 1: The Speed Cache -- LRUCache starter.

See the assignment for full phase-by-phase requirements.
Thread-safety (Phase 3) belongs here too -- wrap get/put bodies in a
single threading.Lock. Don't over-engineer with finer-grained locking.
"""

import threading
from typing import Any, Optional

from doubly_linked_list import DoublyLinkedList, Node

_MISSING = object()  # sentinel distinguishing "not found" from a legitimately-stored None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.map = {}
        self.list = DoublyLinkedList()
        self._lock = threading.Lock()

    def get(self, key: Any) -> Any:
        """
        Return the value for `key` and move it to the most-recently-used
        end, or return the _MISSING sentinel if absent. Both in O(1).
        """
        with self._lock:
            node = self.map.get(key)
            if node is None:
                return _MISSING
            self.list.move_to_front(node)
            return node.value

    def put(self, key: Any, value: Any) -> None:
        """
        Insert or update `key`, moving it to the most-recently-used end.
        If at capacity, evict the least-recently-used entry BEFORE
        inserting the new one. O(1).
        """
        with self._lock:
            node = self.map.get(key)
            if node is not None:
                node.value = value
                self.list.move_to_front(node)
                return

            if len(self.map) >= self.capacity:
                lru = self.list.least_recently_used()
                if lru is not None:
                    self.list.remove(lru)
                    del self.map[lru.key]

            node = Node(key, value)
            self.list.add_to_front(node)
            self.map[key] = node
