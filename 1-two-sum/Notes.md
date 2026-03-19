### Explanation
We need to find two indices such that their values add up to the target.  
The idea is to use a hashmap (dictionary) to store numbers we’ve already seen along with their indices:

- For each number `num` at index `i`, compute `to_find = target - num`.  
- If `to_find` is already in the hashmap, we’ve found the pair → return their indices.  
- Otherwise, store `num` with its index in the hashmap.  

This ensures we only scan the list once.

### Complexity
- **Time:** O(n) — each element is processed once.  
- **Space:** O(n) — in the worst case, all elements are stored in the hashmap.

This approach is efficient and avoids the nested loops of a brute-force solution.
