from abc import ABC, abstractmethod
from typing import Any

class BaseReader(ABC):
    @abstractmethod
    def read(self, content: str) -> list[dict[str, Any]] | dict[str, Any]:
        """Read string content and return data."""
        pass
