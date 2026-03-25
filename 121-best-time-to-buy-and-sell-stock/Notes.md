# Best Time to Buy and Sell Stock

## Explanation
We need to maximize profit by choosing a day to buy and a later day to sell.  
The idea is to track the lowest price seen so far (`buy`) and compute the profit if we sell at the current price (`sell`):

- Initialize `buy = 0`, `sell = 0`, `profit = 0`.
- Iterate through the list with `sell`:
  - Compute `transaction = prices[sell] - prices[buy]`.
  - If `prices[sell] > prices[buy]` and `transaction > profit`, update `profit`.
  - If `prices[sell] < prices[buy]`, update `buy = sell` (new minimum price).
- Continue until the end of the list.
- Return the maximum `profit`.

This ensures we only scan the list once and always consider the best buying opportunity before selling.

---

## Example Walkthrough
`prices = [7, 1, 5, 3, 6, 4]`

1. `buy = 0 (7)`, `sell = 0`, `profit = 0`.
2. `sell = 1 → price=1 < 7` → update `buy = 1`.
3. `sell = 2 → transaction = 5 - 1 = 4` → update `profit = 4`.
4. `sell = 3 → transaction = 3 - 1 = 2` → no update.
5. `sell = 4 → transaction = 6 - 1 = 5` → update `profit = 5`.
6. `sell = 5 → transaction = 4 - 1 = 3` → no update.

Final answer: `profit = 5`.

---

## Complexity
- **Time:** \(O(n)\) — each element is processed once.
- **Space:** \(O(1)\) — only a few variables are tracked.
