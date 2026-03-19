<h2>valid-anagram Notes</h2><hr>[ Time taken: 5m 7s ]

### Explanation
We need to check if two strings are anagrams (contain the same characters with the same frequency).  
Using Python’s `collections.Counter` makes this straightforward:

- `Counter(s)` builds a frequency map of characters in `s`.  
- `Counter(t)` does the same for `t`.  
- If both maps are equal, the strings are anagrams.

### Complexity
- **Time:** O(n) — each string is scanned once to build the frequency map.  
- **Space:** O(n) — additional storage for the character counts.

This approach is clean, efficient, and leverages Python’s built-in data structures for clarity.
