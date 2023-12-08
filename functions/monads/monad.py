"""
A MONOID is a set of elements with a binary operation (It combines two elements that produces a third).
It is associative, so the order in which we combine the two elements does not alter the result.
It should be an identity element: If we pick one of the two elements as a particular value, and then it should result
in the same element.

A MONAD is a specific type of endofunctor (Is a monoid in the domain of endofunctors).
Encapsulates a value, provides a mechanism for doing something with that value.
That mechanism maps back to the same category. It preserves composition.
A monad is a monoid.
"""
from __future__ import annotations

from typing import Generic, Callable, Any, TypeVar


# Monoid: takes two elements and returns a third. Associative. There is an identity element (0+0=0)
def add(x, y) -> int:
    return x + y


def add_one(x: int) -> int:
    return x + 1


def multiply_by_two(x: int) -> int:
    return x * 2


T = TypeVar("T")
U = TypeVar("U")


class Monad(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def bind(self, func: Callable[[T], Monad[U]]) -> Monad[U]:
        return func(self.value)

    @staticmethod
    def unit(value: Any) -> Monad[Any]:
        return Monad(value)


monad = Monad(5)
print(monad.value)
monad2 = monad.bind(lambda x: Monad(add(x, 10)))
print(monad2.value)
# The result has to be the same as applying those two operations without using monads - >
# We can encapsulate side effects in the value of a monad object
monad3 = monad.bind(lambda x: Monad(add_one(x))).bind(lambda x: Monad(multiply_by_two(x))).value
print(monad3)
