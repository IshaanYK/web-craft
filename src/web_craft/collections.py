"""
Web collection manipulation utilities: deep clone, group_by, chunk.
"""

from typing import List, Dict, Any, Callable

def chunk_list(items: List[Any], size: int) -> List[List[Any]]:
    """Splits a list into chunks of designated maximum size."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than 0")
    return [items[i:i + size] for i in range(0, len(items), size)]

def group_by(items: List[Dict[str, Any]], key: str) -> Dict[Any, List[Dict[str, Any]]]:
    """Groups list of dictionaries by key value."""
    result = {}
    for item in items:
        val = item.get(key)
        if val not in result:
            result[val] = []
        result[val].append(item)
    return result

def pick(obj: Dict[str, Any], keys: List[str]) -> Dict[str, Any]:
    """Creates a dictionary composed of the picked object keys."""
    return {k: obj[k] for k in keys if k in obj}
