### Explanation
We need to group words that are anagrams of each other.  
The idea is to use a hashmap (dictionary) where the **key** is a canonical representation of the word, and the **value** is a list of words that match that key.

- For each string in the input list:
  - Sort the characters to form a key (e.g., `"eat"` → `"aet"`).  
  - If the key is not in the hashmap, initialize it with the current word.  
  - Otherwise, append the word to the existing list for that key.  

- Finally, return all the grouped lists of words.

### Complexity
- **Time:** O(n · k log k)  
  - `n` = number of strings  
  - `k` = maximum length of a string  
  - Sorting each string takes O(k log k), repeated for all `n` strings.  
- **Space:** O(n · k) — storing all strings in the hashmap.

This approach is intuitive and leverages sorting to normalize anagrams into the same key.
