from typing import Any


class ContextManager:
    def __enter__(self) -> Any:
        return Any

    def __exit__(self, exc_type, exc_value, traceback) -> bool | None:
        pass
