### Explanation
The task is to check if a string is a palindrome, considering only alphanumeric characters and ignoring cases.

Steps:
- Iterate through the string and build a cleaned version (`rev`) containing only lowercase alphanumeric characters.  
- Compare the cleaned string with its reverse (`rev[::-1]`).  
- If they match, the string is a palindrome.

### Complexity
- **Time:** O(n) — we scan the string once and perform a reverse comparison.  
- **Space:** O(n) — storing the cleaned string.

This approach is straightforward, readable, and leverages Python’s string handling to normalize and check palindromes efficiently.
