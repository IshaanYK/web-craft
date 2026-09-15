"""
Unit tests for web utility functions.
"""

import unittest
from web_craft.collections import chunk_list, group_by, pick
from web_craft.url_params import stringify_query, parse_query

class TestWebCraft(unittest.TestCase):
    def test_collections(self):
        self.assertEqual(chunk_list([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])
        users = [{'role': 'admin', 'name': 'Alice'}, {'role': 'user', 'name': 'Bob'}]
        grouped = group_by(users, 'role')
        self.assertEqual(len(grouped['admin']), 1)
        self.assertEqual(pick({'a': 1, 'b': 2, 'c': 3}, ['a', 'c']), {'a': 1, 'c': 3})

    def test_url_params(self):
        query = stringify_query({'q': 'search query', 'page': 2, 'filter': None})
        self.assertEqual(query, "q=search+query&page=2")
        parsed = parse_query(query)
        self.assertEqual(parsed['page'], '2')

if __name__ == '__main__':
    unittest.main()
