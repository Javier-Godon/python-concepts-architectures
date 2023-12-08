from __future__ import annotations

from typing import Generic, Callable, Any, TypeVar, Optional

T = TypeVar("T")
U = TypeVar("U")


class Maybe(Generic[T]):
    def __init__(self, value: Optional[T]) -> None:
        self.value = value

    def bind(self, func: Callable[[T], Maybe[U]]) -> Maybe[U]:
        return self if self.value is None else func(self.value)

    @staticmethod
    def unit(value: Any) -> Maybe[Any]:
        return Maybe(value)


def safe_divide(x: float, y: float) -> Maybe[float]:
    return Maybe(None) if y == 0 else Maybe(x / y)


'''
Railroad-oriented programming
'''
result = Maybe(10).bind(lambda x: safe_divide(x, 0)).bind(lambda x: safe_divide(x, 2))
print(result.value)
result = Maybe(10).bind(lambda x: safe_divide(x, 2)).bind(lambda x: safe_divide(x, 2))
print(result.value)
