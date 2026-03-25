# Rotate String
<h2>rotate-string Notes</h2><hr>[ Time taken: 6m 41s ]

## How It Works
The problem asks whether one string can be rotated to become another.  
A rotation means shifting characters from the front of the string to the back while keeping the order intact.

### Key Insight
If `goal` is a rotation of `s`, then `goal` must appear as a substring of `s + s`.

- Example:  
  `s = "abcde"`  
  All rotations are: `"bcdea"`, `"cdeab"`, `"deabc"`, `"eabcd"`.  
  If we concatenate `s + s = "abcdeabcde"`, all possible rotations of `s` are contained inside this doubled string.  
  So checking if `goal` is inside `s + s` tells us if it’s a valid rotation.

### Step-by-Step Logic
1. **Length Check**  
   If `s` and `goal` don’t have the same length, they can’t be rotations → return `False`.

2. **Concatenate**  
   Build `s + s`. This string contains every possible rotation of `s`.

3. **Substring Search**  
   If `goal` is found inside `s + s`, return `True`.  
   Otherwise, return `False`.

---

## Example Walkthrough
`s = "abcde"`, `goal = "cdeab"`

1. Lengths match → continue.  
2. `s + s = "abcdeabcde"`.  
3. Check if `"cdeab"` is in `"abcdeabcde"`.  
4. It is → return `True`.

---

## Complexity
- **Time:** \(O(n)\) — substring search runs in linear time relative to string length.  
- **Space:** \(O(n)\) — due to storing `s + s`.

---

## Why It’s Elegant
Instead of manually simulating rotations (which would take \(O(n^2)\)), the trick of doubling the string reduces the problem to a simple substring search. This is both efficient and easy to implement.
