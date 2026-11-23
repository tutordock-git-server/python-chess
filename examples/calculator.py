#!/usr/bin/env python3

"""A basic calculator with simple operations and an interactive prompt.

Usage:
    python3 examples/calculator.py          # interactive mode
    python3 examples/calculator.py 2 + 3    # one-shot calculation
"""

from __future__ import annotations

import operator
import sys
from typing import Callable

OPERATIONS: dict[str, Callable[[float, float], float]] = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def calculate(left: float, op: str, right: float) -> float:
    """Apply one of the four basic arithmetic operations."""
    try:
        operation = OPERATIONS[op]
    except KeyError:
        raise ValueError(f"Unsupported operator: {op!r}") from None
    return operation(left, right)


def parse_number(value: str) -> float:
    """Convert text to an integer when possible, otherwise a float."""
    try:
        return int(value)
    except ValueError:
        return float(value)


def main(argv: list[str]) -> int:
    if argv:
        if len(argv) != 3:
            print("Usage: calculator.py <number> <operator> <number>", file=sys.stderr)
            return 2
        try:
            result = calculate(parse_number(argv[0]), argv[1], parse_number(argv[2]))
        except (ValueError, ZeroDivisionError) as error:
            print(f"Error: {error}", file=sys.stderr)
            return 1
        print(result)
        return 0

    print("Basic calculator. Enter 'quit' to exit.")
    while True:
        try:
            expression = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0

        if expression.lower() in ("quit", "exit"):
            return 0
        if not expression:
            continue

        parts = expression.split()
        if len(parts) != 3:
            print("Enter an expression like: 2 + 3")
            continue
        try:
            result = calculate(parse_number(parts[0]), parts[1], parse_number(parts[2]))
        except (ValueError, ZeroDivisionError) as error:
            print(f"Error: {error}")
            continue
        print(result)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
 # you added successfully