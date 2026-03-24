### Explanation
The input array is already sorted, which allows us to use the **two-pointer technique**:

- Initialize two pointers:  
  - `low` at the start of the array  
  - `high` at the end of the array  
- Compute the sum of the two pointers:  
  - If the sum equals the target → return the indices (1-based).  
  - If the sum is less than the target → move `low` forward to increase the sum.  
  - If the sum is greater than the target → move `high` backward to decrease the sum.  
- Continue until the correct pair is found.

This avoids nested loops and leverages the sorted property of the array.

### Complexity
- **Time:** O(n) — each element is visited at most once by either pointer.  
- **Space:** O(1) — only two pointers are used.

This approach is efficient and elegant, making full use of the sorted input.
