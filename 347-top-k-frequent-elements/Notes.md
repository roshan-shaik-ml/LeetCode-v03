### Explanation
The task is to find the `k` most frequent elements in the array.  

Steps:
- Build a frequency map of all elements using `Counter(nums)`.  
- Sort the items of the map by their frequency in descending order.  
- Slice the first `k` items and return their keys.  

This ensures we directly get the top `k` frequent elements.

### Complexity
- **Time:** O(n log n) — building the frequency map takes O(n), and sorting the map items takes O(n log n).  
- **Space:** O(n) — storing the frequency map.

This solution is concise, readable, and leverages Python’s built-in sorting.

---

### Alternative Approach
Instead of sorting the entire frequency map:
- Use a **heap** (`heapq.nlargest`) to efficiently extract the top `k` elements without fully sorting.  
- Or use `Counter.most_common(k)`, which directly returns the top `k` frequent elements.  

These alternatives are more efficient when `k` is much smaller than `n`, since they avoid sorting all items.
