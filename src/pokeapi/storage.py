from typing import Any, Optional


class InMemoryStorage:
    def __init__(self) -> None:
        self._storage: dict[str, Any] = {}

    def get(self, key: str) -> Optional[Any]:
        return self._storage.get(key)

    def set(self, key: str, value: Any) -> None:  # noqa: 110
        self._storage[key] = value

    def clear(self) -> None:
        self._storage.clear()
