<h2>contains-duplicate Notes</h2><hr>[ Time taken: 32s ]


### Explanation
A `set` automatically removes duplicates.

If the length of the set is smaller than the length of the original list, it means duplicates were present.

This gives a direct one-line solution.

### Complexity
- **Time:** O(n) — building the set requires scanning all elements.  
- **Space:** O(n) — in the worst case, all elements are unique and stored in the set.

This approach is concise, efficient, and leverages Python’s data structures to avoid manual iteration.
