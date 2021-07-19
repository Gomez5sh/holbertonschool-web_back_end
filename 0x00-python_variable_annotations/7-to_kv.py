
#!/usr/bin/env python3
""" string and int/float to tuple"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    >>> to_kv('foo', 1)
    """
    return (k, v * v)
