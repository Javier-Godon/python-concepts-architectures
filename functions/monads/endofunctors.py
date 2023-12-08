"""
functor: combination of:
         - value
         - mechanism to do something with that value
returns a new functor containing that process that changes that value

endofunctor: functor that has the same shape (same combination of the two things, value and method)
as the original functor that the method was called on.
"""
from typing import Any, Callable


class Functor:
    def __init__(self, value: Any) -> None:
        self.value = value

    def map(self, func: Callable[[Any], Any]):
        return Functor(func(self.value))


# This is a functor but not an endofunctor
class StringFunctor:
    def __init__(self, value: str) -> None:
        self.value = value

    def map(self, func: Callable[[str], str]):
        return ListFunctor([func(self.value)])


# This is an endofunctor
class ListFunctor:
    def __init__(self, values: list[Any]):
        self.values = values

    def map(self, func: Callable[[Any], Any]):
        return ListFunctor([func(value) for value in self.values])


def add_one(x: int) -> int:
    return x + 1


def multiply_by_two(x: int) -> int:
    return x * 2


f = Functor(5)
# Mapping within the same category
g = f.map(add_one)

print(f.value)
print(g.value)

# Preserves structure
assert isinstance(g, Functor)

# Preserves composition
assert (
        f.map(add_one).map(multiply_by_two).value == f.map(lambda x: multiply_by_two(add_one(x))).value
)
