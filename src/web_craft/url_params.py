"""
URL query string parsing and serialization utilities.
"""

import urllib.parse
from typing import Dict, Any

def stringify_query(params: Dict[str, Any]) -> str:
    """Serializes a dictionary of query parameters into a URL query string."""
    clean_params = {}
    for k, v in params.items():
        if v is not None:
            clean_params[k] = str(v)
    return urllib.parse.urlencode(clean_params)

def parse_query(query_str: str) -> Dict[str, str]:
    """Parses a URL query string into a key-value dictionary."""
    if query_str.startswith('?'):
        query_str = query_str[1:]
    parsed = urllib.parse.parse_qs(query_str)
    return {k: v[0] for k, v in parsed.items()}
